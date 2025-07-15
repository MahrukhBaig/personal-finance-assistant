import streamlit as st
import matplotlib.pyplot as plt
from datetime import date
import pandas as pd
from finance_utils import (
    parse_message,
    save_transaction,
    get_summary,
    get_category_report,
    get_saving_tip,
    get_daily_summary,       
    get_weekly_summary,       
)

st.set_page_config(page_title="Personal Finance Chatbot", page_icon="💸")
st.title("💬 Personal Finance Assistant")
st.write("Ask me to track expenses, show summaries, or give saving tips!")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input text box
user_input = st.text_input("You:", placeholder="Type your message here...")

# Buttons
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
submit_clicked = col1.button("Submit")
clear_clicked = col2.button("Clear History 🗑️")
daily_clicked = col3.button("📅 Daily Summary")
weekly_clicked = col4.button("🗓️ Weekly Summary")


# Clear history button action
if clear_clicked:
    st.session_state.chat_history = []

# Daily summary button
if daily_clicked:
    response = get_daily_summary()
    st.session_state.chat_history.append(("Bot", response))

# Weekly summary button
if weekly_clicked:
    response = get_weekly_summary()
    st.session_state.chat_history.append(("Bot", response))

# Process input when Submit is clicked
if submit_clicked and user_input.strip():
    msg = user_input.strip()

    # Determine response
    if msg.lower() in ["exit", "quit", "bye", "stop"]:
        response = "👋 Goodbye! Stay financially smart 💡"
    elif msg.lower() in ["summary", "get summary", "show summary", "monthly summary", "give me my monthly summary","weekly summary","day_summary"]:
        response = get_summary()
    elif "how much" in msg.lower() or "did i spend" in msg.lower():
        response = get_category_report(msg)
    elif "tip" in msg.lower() or "advice" in msg.lower() or "saving" in msg.lower():
        response = get_saving_tip()
    else:
        parsed = parse_message(msg)
        if parsed["type"] == "unknown":
            response = "🤖 Sorry, I couldn't understand that. Please enter an expense or income."
        else:
            save_transaction(parsed)
            response = f" Added {parsed['amount']} to '{parsed['category']}' as a {parsed['type']}."

    # Add message + response to chat history
    st.session_state.chat_history.append(("You", msg))
    st.session_state.chat_history.append(("Bot", response))

# Show chat history (scrollable)
with st.container():
    for speaker, text in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f"**🧍 You:** {text}")
        else:
            st.markdown(f"**🤖 Bot:** {text}")


st.markdown("---")
st.subheader("📊 Visualize Expenses")

months = [''] + list(pd.date_range(start='2024-01-01', end=date.today(), freq='M').strftime('%B').unique())
selected_month = st.selectbox("Select Month to Filter (optional):", months)

if st.button("Show Bar Chart"):
    from finance_utils import get_expense_bar_chart
    fig, err = get_expense_bar_chart(month=selected_month if selected_month else None)
    if err:
        st.warning(err)
    else:
        st.pyplot(fig)

import re
import datetime
import pandas as pd
import random

# Simple category mapping
CATEGORY_KEYWORDS = {
    "food": "groceries",
    "grocery": "groceries",
    "groceries": "groceries",
    "rent": "rent",
    "travel": "transport",
    "bus": "transport",
    "uber": "transport",
    "salary": "salary",
    "bonus": "salary",
    "shopping": "shopping",
    "clothes": "shopping",
    "utilities": "bills",
    "electricity": "bills",
    "internet": "bills",
    "phone": "bills",
    "hospital": "health",
    "medicines": "health",

}

def parse_message(msg: str):
    msg = msg.lower()

    # Extract amount using regex
    amount_match = re.search(r'\d+', msg)
    amount = float(amount_match.group()) if amount_match else 0

    # Determine type
    if any(word in msg for word in ["spent", "bought", "paid", "on", "billed"]):
        entry_type = "expense"
    elif any(word in msg for word in ["earned", "got", "salary", "income", "received"]):
        entry_type = "income"
    else:
        entry_type = "unknown"

    # Detect category
    category = "misc"
    for keyword, mapped in CATEGORY_KEYWORDS.items():
        if keyword in msg:
            category = mapped
            break

    return {
        "amount": amount,
        "category": category,
        "type": entry_type,
        "date": datetime.date.today()
    }
    
  
def save_transaction(data: dict, file_path='finance_data.csv'):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["amount", "category", "type", "date"])

    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(file_path, index=False)


def get_summary(file_path='finance_data.csv'):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return "No transactions yet!"

    total_income = df[df["type"] == "income"]["amount"].sum()
    total_expense = df[df["type"] == "expense"]["amount"].sum()
    balance = total_income - total_expense

    return f"""
 Your Financial Summary:
- Total Income: {total_income:,}
- Total Expense: {total_expense:,}
- Net Savings: {balance:,}
"""
import datetime

def get_daily_summary(file_path='finance_data.csv'):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return "No transactions yet!"

    today = datetime.date.today().strftime('%Y-%m-%d')
    daily_df = df[df['date'] == today]

    if daily_df.empty:
        return "No transactions found for today."

    total_income = daily_df[daily_df["type"] == "income"]["amount"].sum()
    total_expense = daily_df[daily_df["type"] == "expense"]["amount"].sum()
    balance = total_income - total_expense

    return f"""
📅 **Today's Summary ({today})**
- Income: {total_income}
- Expenses: {total_expense}
- Net: {balance}
"""

def get_weekly_summary(file_path='finance_data.csv'):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return "No transactions yet!"

    df['date'] = pd.to_datetime(df['date'])
    one_week_ago = pd.to_datetime(datetime.date.today()) - pd.Timedelta(days=7)
    weekly_df = df[df['date'] >= one_week_ago]

    if weekly_df.empty:
        return "No transactions in the last 7 days."

    total_income = weekly_df[weekly_df["type"] == "income"]["amount"].sum()
    total_expense = weekly_df[weekly_df["type"] == "expense"]["amount"].sum()
    balance = total_income - total_expense

    return f"""
🗓️ **This Week's Summary**
- Income: {total_income}
- Expenses: {total_expense}
- Net: {balance}
"""

def get_category_report(msg, file_path='finance_data.csv'):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return "No transactions available."

    msg = msg.lower()
    
    # Match user's message to a category
    for keyword, category in CATEGORY_KEYWORDS.items():
        if keyword in msg:
            # Get total for that category
            total = df[df["category"] == category]["amount"].sum()
            return f"You’ve spent a total of {total} on {category}."
    
    return "Sorry, I couldn’t detect a valid category in your question."

def get_saving_tip(file_path='saving_tips.txt'):
    try:
        with open(file_path, 'r') as f:
            tips = f.readlines()
            if not tips:
                return "No tips available right now."
            return "Saving Tip: " + random.choice(tips).strip()
    except FileNotFoundError:
        return " Couldn’t find saving tips file."
    
# Add this to finance_utils.py
import matplotlib.pyplot as plt

def get_expense_bar_chart(month=None, file_path='finance_data.csv'):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return None, "No transactions yet!"

    df['date'] = pd.to_datetime(df['date'])
    df = df[df['type'] == 'expense']

    if month:
        df = df[df['date'].dt.strftime('%B').str.lower() == month.lower()]
        if df.empty:
            return None, f"No expenses found for {month.title()}."

    grouped = df.groupby('category')['amount'].sum().sort_values(ascending=False)

    if grouped.empty:
        return None, "No expense data to plot."

    fig, ax = plt.subplots()
    grouped.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title(f'Expenses by Category{" - " + month.title() if month else ""}')
    ax.set_ylabel('Amount')
    ax.set_xlabel('Category')

    return fig, None
    
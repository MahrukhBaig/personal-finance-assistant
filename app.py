from finance_utils import (
    parse_message,
    save_transaction,
    get_summary,
    get_category_report,
    get_daily_summary,     
    get_weekly_summary,
    get_saving_tip  
)

print("Welcome to your Personal Finance Assistant 💬")
print("Type 'summary' anytime to view your financial overview.\n")

exit_commands = ["exit", "quit", "bye", "stop", "close"]

while True:
    msg = input("You: ")

    if msg.lower() in exit_commands:
        print("Goodbye! Stay financially smart 💡")
        break

    elif msg.lower() in ["summary", "get summary", "show summary"]:
        print(get_summary())
        continue

    elif msg.lower() in ["daily summary", "today summary", "day summary"]:
        print(get_daily_summary())
        continue

    elif msg.lower() in ["weekly summary", "this week", "week summary"]:
        print(get_weekly_summary())
        continue

    elif "how much" in msg.lower() or "did i spend" in msg.lower():
        print(get_category_report(msg))
        continue

    elif "tip" in msg.lower() or "advice" in msg.lower() or "saving" in msg.lower():
        print(get_saving_tip())
        continue

    parsed = parse_message(msg)
    if parsed['type'] == "unknown":
        print("🤖 Sorry, I couldn't understand that. Please enter an expense or income.")
        continue

    save_transaction(parsed)
    print(f" Added {parsed['amount']} to {parsed['category']} as a {parsed['type']}.")

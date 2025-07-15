---

## 💸 Personal Finance Assistant Chatbot

Personal Finance Assistant is a conversational chatbot built using Python and Streamlit, designed to make expense and income tracking as simple as having a chat.

Instead of filling out spreadsheets or using complex finance tools, users can interact with the bot by typing natural language messages
---

### 🚀 Live Demo

[Click here to try it on Streamlit!](https://personal-finance-assistant-ab8mmcvvsukqrqhce77kv4.streamlit.app/)

---

### 📂 Features

* ✅ Add income and expenses via natural text input
* 📊 View daily, weekly, and full financial summaries
* 📁 Stores data in a local CSV file (`finance_data.csv`)
* 🔍 Category-based spending queries (e.g., "how much did I spend on food?")
* 💡 Random saving tips
* 📅 View visual spending summary by month (optional extension)
* 🧠 Budget alert system (if added)

---

### 🛠️ Technologies Used

* **Python 3.10+**
* **Streamlit**
* **Pandas**
* **Regex** for message parsing

---

### 📥 Getting Started

#### Clone the Repo

```bash
git clone https://github.com/MahrukhBaig/personal-finance-assistant.git
cd personal-finance-assistant
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Run the App Locally

```bash
streamlit run streamlit_app.py
```

---

### 📁 Folder Structure

```
📦 personal-finance-assistant
├── streamlit_app.py          # Streamlit-based frontend
├── finance_utils.py          # Core logic and backend functions
├── app.py                    # CLI version (optional)
├── saving_tips.txt           # Optional: list of random saving tips
├── finance_data.csv          # Auto-generated log file
└── requirements.txt
```

---

### 🧠 Example Inputs You Can Try

* `"I spent 100 on groceries"`
* `"Received salary 50000"`
* `"Give me a saving tip"`
* `"how much did I spend on transport"`
* `"summary"`
* `"weekly summary"`
* `"daily summary"`

---

### ✨ Author

**Mahrukh Baig**
📧 [baigmahrukh8@gmail.com](mailto:baigmahrukh8@gmail.com)
🔗 [GitHub Profile](https://github.com/MahrukhBaig)



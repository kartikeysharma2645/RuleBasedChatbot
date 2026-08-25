# CodeOrbit Rule-Based Chatbot

A beginner-friendly rule-based chatbot built with Python using predefined keywords, phrases, and conditional logic to generate responses.

This project was developed as **Task 1** of the **CodeOrbit Tech – Artificial Intelligence (AI) Internship**.

---

## 📌 Project Overview

This project demonstrates the basic working principle of a rule-based chatbot.

The chatbot accepts user input, normalizes the text, checks it against predefined rules, and generates an appropriate response. If no rule matches the input, the chatbot provides a fallback response.

The project intentionally uses fundamental Python concepts such as `if-elif-else`, loops, string processing, and keyword matching instead of machine learning or external AI models.

---

## ✨ Features

- Responds to common greetings such as `hello`, `hi`, and `hey`
- Answers predefined questions about itself
- Provides basic information about Python, Artificial Intelligence, and Machine Learning
- Handles conversational inputs such as thanks and jokes
- Responds to help and capability-related questions
- Supports multiple exit commands
- Uses exact phrase and keyword-based matching
- Normalizes user input by converting it to lowercase and removing extra whitespace and punctuation
- Provides a fallback response for unrecognized inputs
- Runs continuously until the user exits

---

## ⚙️ How It Works

The chatbot follows a simple rule-based decision process:

```text
User Input
    ↓
Normalize Input
    ↓
Check Predefined Rules
    ↓
Find First Matching Rule
    ↓
Generate Response
    ↓
Continue Conversation
    ↓
No Match → Fallback Response
```

### Input Normalization

Before checking the rules, the chatbot:

1. Converts the input to lowercase.
2. Removes leading and trailing whitespace.
3. Removes trailing `!` and `?` characters.

This allows inputs such as:

```text
HELLO
Hello!!
hello
```

to be handled consistently.

### Rule Matching

The chatbot uses different types of matching:

- **Exact matching** for specific commands and questions.
- **Phrase matching** for conversational patterns.
- **Keyword matching** for broader topics.

For example:

```python
elif "python" in user_input:
    print("Bot: Python is a high-level, general-purpose programming language.")
```

This allows different inputs containing the keyword `python` to trigger the same predefined response.

When multiple rules could match an input, the chatbot evaluates the rules from top to bottom and uses the **first matching condition**.

---

## 💬 Supported Interactions

| Category | Example |
|---|---|
| Greetings | `hello`, `hi`, `hey` |
| Identity | `what is your name` |
| Capabilities | `what can you do` |
| Status | `how are you` |
| Creator | `who created you`, `who made you` |
| Purpose | `what is your purpose`, `why were you created` |
| Python | `tell me about Python` |
| Artificial Intelligence | `what is AI` |
| Machine Learning | `what is machine learning` |
| Help | `help` |
| Thanks | `thank you` |
| Jokes | `tell me a joke` |
| Time | `what time is it` |
| Exit | `bye`, `goodbye`, `see you` |
| Unknown Input | Fallback response |

---

## 🛠️ Technologies Used

- **Python 3**
- Conditional statements (`if`, `elif`, `else`)
- `while` loop
- String processing
- Keyword and phrase matching
- Python built-in functions

**No external libraries or packages are required.**

---

## 📁 Project Structure

```text
CodeOrbit_RuleBasedChatbot/
│
├── chatbot.py
├── README.md
└── .gitignore
```

### File Description

- **`chatbot.py`** — Contains the complete chatbot implementation.
- **`README.md`** — Contains project documentation and usage instructions.
- **`.gitignore`** — Prevents unnecessary Python-generated and local environment files from being committed.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

Clone the repository:

```bash
git clone https://github.com/kartikeysharma2645/CodeOrbit_RuleBasedChatbot.git
```

Navigate to the project directory:

```bash
cd CodeOrbit_RuleBasedChatbot
```

### Run the Chatbot

```bash
python chatbot.py
```

If your system uses `python3`:

```bash
python3 chatbot.py
```

---

## 🧪 Example Interaction

```text
You: hello
Bot: Hello! How can I help you?

You: What is Python?
Bot: Python is a high-level, general-purpose programming language.

You: What is AI?
Bot: Artificial Intelligence is the field of creating systems that can perform tasks that normally require human intelligence.

You: Tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: thank you
Bot: You're welcome!

You: see you later
Bot: Goodbye!
```

---

## ⚠️ Limitations

This chatbot uses predefined rules rather than machine learning or generative AI.

Therefore, it:

- Cannot understand conversation context or intent.
- Can only respond to inputs covered by its predefined rules.
- May not recognize differently phrased questions.
- Uses the first matching rule when multiple rules apply.

These limitations are intentional because the project is designed to demonstrate the fundamentals of rule-based chatbot development.

---

## 🎯 Internship Task

**Program:** CodeOrbit Tech – Artificial Intelligence (AI) Internship  
**Task:** Task 1 – Rule-Based Chatbot

### Requirements Implemented

- ✅ Rule-based chatbot
- ✅ Predefined rules and keywords
- ✅ Common greetings
- ✅ Questions and predefined responses
- ✅ Fallback response
- ✅ Python implementation
- ✅ `if-elif-else` decision logic
- ✅ Comments explaining chatbot decision logic
- ✅ Continuous user interaction
- ✅ Exit condition

---

## 👨‍💻 Author

**Kartikey Sharma**

Developed as part of the **CodeOrbit Tech – Artificial Intelligence (AI) Internship**.

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub!
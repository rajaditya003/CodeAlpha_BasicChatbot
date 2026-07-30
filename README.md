# Basic Chatbot 🤖

**Project:** Basic Chatbot  
**Internship:** CodeAlpha Python Internship  
**Author:** Aashu Raj  

---

## Overview

The **Basic Chatbot** is a terminal-based conversational application written entirely in Python. It interacts continuously with the user by recognizing standard greetings and basic questions, and responds with predefined friendly messages. It demonstrates foundational programming concepts such as loops, conditional statements, string manipulation, and modular functions.

## Features

- **Continuous Interaction**: Runs in a loop until the user types `bye`, `exit`, or `quit`.
- **Predefined Conversations**: Understands common phrases like "hello", "how are you", "what is your name", "who created you", and more.
- **Robust Input Validation**: Gracefully handles:
  - Empty inputs (pressing enter without typing)
  - Extra leading/trailing spaces
  - Mixed uppercase and lowercase letters (case-insensitive matching)
- **Randomized Greetings**: Provides varied responses for basic greetings.
- **Modular Design**: Broken down into focused functions for easier readability and maintenance.

## Technologies Used

- **Python 3.x**: Core programming language.
- **Standard Library**: Uses only built-in tools (e.g., `random`), requiring no external dependencies.

## Folder Structure

```text
Basic-Chatbot/
│── chatbot.py      # The main chatbot Python script
│── README.md       # Project documentation (this file)
```

## How to Run

1. Make sure you have Python installed on your computer.
2. Open your terminal or command prompt.
3. Navigate to the project directory:
   ```bash
   cd Basic-Chatbot
   ```
4. Run the script:
   ```bash
   python chatbot.py
   ```

## Sample Conversation

```text
==================================================
           🤖 WELCOME TO BASIC CHATBOT 🤖
==================================================
Type 'bye', 'exit', or 'quit' to end the chat.
--------------------------------------------------

You: Hello
🤖 Chatbot: Hi! How can I help you today?

You: What is your name?
🤖 Chatbot: I am Basic Chatbot, your friendly virtual assistant.

You: How are you
🤖 Chatbot: I'm just a computer program, but I'm feeling fantastic! How are you?

You:     who created you    
🤖 Chatbot: I was created by Aashu Raj for the CodeAlpha Python Internship.

You: Thank you!
🤖 Chatbot: Sorry, I don't understand that yet.

You: thank you
🤖 Chatbot: You're very welcome! I'm happy to help.

You: 
🤖 Chatbot: Please say something! I'm listening.

You: exit
--------------------------------------------------
🤖 Chatbot: Thank you for chatting. Have a wonderful day!
==================================================
```

## Learning Outcomes

By building this project, beginners will learn how to:
- Use **while loops** for continuous program execution.
- Implement complex **if-elif-else** statements for decision making.
- Manipulate strings using methods like `.strip()` and `.lower()`.
- Define and call custom **functions** (`chat()`, `get_response()`).
- Handle user input securely and deal with edge cases (like empty strings).

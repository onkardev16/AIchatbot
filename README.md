# 🤖 EduBot — AI Chatbot with GUI

> **An intelligent chatbot for college students** built with Python, NLTK, Tkinter, and SQLite.
> Submitted as part of the Artificial Intelligence / Python Programming course project.

---

## 📌 Project Overview

EduBot is a rule-based AI chatbot that uses **Natural Language Processing (NLP)** to understand and respond to user messages. It features a sleek dark-mode GUI with voice input/output, typing animations, and persistent chat history.

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 🧠 NLP Engine | NLTK tokenization, lemmatization, and intent matching |
| 🌙 Dark / Light Mode | Toggle with one click |
| 🎙️ Voice Input | Speak your query (SpeechRecognition) |
| 🔊 Voice Output | Bot speaks back (pyttsx3 TTS) |
| ⌨️ Typing Animation | Realistic character-by-character response |
| 💾 Chat History | All messages stored in SQLite database |
| 🗑️ Clear Chat | One-click clear with confirmation dialog |
| ⚡ Quick Actions | Sidebar buttons for common queries |
| 📱 Responsive Layout | Adapts to window resizing |

---

## 📁 Project Structure

```
ai_chatbot/
│
├── main.py                  ← Entry point (run this!)
├── requirements.txt         ← Python dependencies
├── README.md                ← This file
│
├── chatbot/
│   ├── __init__.py
│   ├── bot_engine.py        ← NLP + Intent matching + Response generation
│   └── voice_handler.py     ← TTS (pyttsx3) + STT (SpeechRecognition)
│
├── database/
│   ├── __init__.py
│   ├── db_handler.py        ← SQLite operations (save, load, clear)
│   └── chat_history.db      ← Auto-created on first run
│
├── gui/
│   ├── __init__.py
│   └── chat_window.py       ← Main Tkinter GUI (all visual components)
│
└── assets/                  ← Optional: icons, images
```

---

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Core programming language |
| **Tkinter** | GUI framework (built into Python) |
| **NLTK** | NLP — tokenization, lemmatization, stopwords |
| **SQLite3** | Persistent chat history storage |
| **pyttsx3** | Text-to-Speech (offline) |
| **SpeechRecognition** | Speech-to-Text (voice input) |
| **threading** | Non-blocking background tasks |

---

## 🚀 Setup & Run Instructions

### Step 1 — Clone / Download
```bash
# Download and unzip the project, then:
cd ai_chatbot
```

### Step 2 — Install Python (if not installed)
Download from https://python.org  
Minimum version: **Python 3.8**

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note:** If `pyaudio` fails to install (common on Windows):
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```
> Voice input is optional — the chatbot works without it.

### Step 4 — Run the Chatbot
```bash
python main.py
```

That's it! The GUI will open automatically. The SQLite database is created automatically on first run.

---

## 💬 Sample Conversations

```
You:    hello
EduBot: Hello! 👋 How can I help you today?

You:    what time is it?
EduBot: 🕐 The current time is 03:45 PM

You:    tell me about courses
EduBot: 📚 Available Engineering Branches:
        • Computer Science Engineering (CSE)
        • Information Technology (IT)
        • Mechanical Engineering (ME)
        ...

You:    how do i apply for admission?
EduBot: 📋 Admission Process:
        1. Visit the official college website.
        2. Fill out the online application form.
        ...

You:    tell me a joke
EduBot: 😂 Why do programmers prefer dark mode?
        Because light attracts bugs!

You:    motivate me
EduBot: 💪 "The secret of getting ahead is getting started." — Mark Twain

You:    bye
EduBot: Goodbye! 👋 Have a wonderful day!
```

---

## 🧠 How the NLP Works

```
User Input
    │
    ▼
Tokenization (split into words)
    │
    ▼
Lemmatization (run → run, running → run)
    │
    ▼
Keyword Matching (compare against intent patterns)
    │
    ▼
Intent Detection (greeting / courses / time / jokes ...)
    │
    ▼
Random Response Selection from matched intent
    │
    ▼
Display in GUI + Save to SQLite + Speak (if voice on)
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE chat_history (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    sender    TEXT NOT NULL,    -- 'User' or 'Bot'
    message   TEXT NOT NULL,    -- Message content
    timestamp TEXT NOT NULL     -- "YYYY-MM-DD HH:MM:SS"
);
```

---

## 🎨 UI Components

| Component | Description |
|---|---|
| **Header Bar** | Logo, title, online status, theme toggle |
| **Chat Area** | Scrollable bubble-style messages |
| **Sidebar** | 10 quick-action buttons + voice toggle |
| **Input Bar** | Text field + mic button + send button |
| **Status Bar** | Session info + character counter |

---

## ❓ Common Viva Questions & Answers

**Q: What is NLP?**  
A: Natural Language Processing — the ability of computers to understand and process human language using algorithms.

**Q: What NLTK functions did you use?**  
A: `word_tokenize()` for splitting text into tokens, `WordNetLemmatizer` for reducing words to their base form, and `stopwords` for filtering common words.

**Q: What is SQLite?**  
A: A lightweight, file-based relational database built into Python via the `sqlite3` module. No server needed.

**Q: How does intent matching work?**  
A: Each intent has a list of pattern keywords. The bot counts how many pattern words appear in the user's tokenized input. The intent with the highest count is selected.

**Q: What is threading used for?**  
A: To run the bot's response generation in a background thread, preventing the GUI from freezing while the bot "thinks."

**Q: What is TTS?**  
A: Text-to-Speech — converting written text to spoken audio using the `pyttsx3` library.

---

## 👨‍💻 Developer Notes

- All code is thoroughly commented for readability.
- Error handling is in place for database operations, voice I/O, and NLTK downloads.
- NLTK data is auto-downloaded on first run.
- The chatbot is easily extensible — add new intents to `INTENTS` in `bot_engine.py`.

---

## 📄 License
This project is for educational purposes. Free to use and modify.

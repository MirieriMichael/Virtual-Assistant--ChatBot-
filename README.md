# 🧠 AI Voice Assistant (Python)

A desktop-based **AI Voice Assistant** built with **Python**, featuring **speech recognition**, **text-to-speech**, **Tkinter GUI**, **rule-based responses**, and **NLP-powered conversational intelligence** using **Hugging Face Transformers**.

This project demonstrates practical integration of **GUI development**, **speech processing**, and **natural language processing (NLP)** — ideal for learning, demos, and portfolio showcasing.

---

## ✨ Features

* 🎤 **Speech-to-Text** (voice input via microphone)
* 🔊 **Text-to-Speech** (spoken AI responses)
* 🖥️ **Tkinter GUI** (interactive desktop interface)
* 📄 **JSON-based predefined responses** (fast & deterministic replies)
* 🤖 **NLP-powered chatbot** (GPT-2 for free-form conversation)
* 😊 **Sentiment Analysis** (DistilBERT via Hugging Face)
* 🌐 **Web commands** (open Google, YouTube, play music)
* 🧩 **Hybrid logic** (rules first → NLP fallback)

---

## 🏗️ Project Structure

```
Virtual Assistant/
│
├── gui.py                     # Tkinter GUI
├── action.py                  # Core logic (rules + NLP)
├── speech_to_txt.py           # Speech recognition
├── text_to_speech.py          # Text-to-speech
│
├── JSON Files/
│   └── responses.json         # Predefined responses
│
├── images/
│   └── chatbot.jpg            # GUI image
│
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. **User speaks** → microphone input
2. **Speech Recognition** converts voice to text
3. **Action engine** processes input:

   * Checks predefined JSON responses
   * Falls back to GPT-2 for free conversation
4. **Optional sentiment analysis**
5. **Text-to-Speech** speaks the response
6. **Conversation displayed in GUI**

---

## 📦 Technologies Used

* **Python 3.10+**
* **Tkinter** – GUI
* **SpeechRecognition** – speech-to-text
* **PyAudio** – microphone input
* **pyttsx3** – text-to-speech
* **Hugging Face Transformers**

  * GPT-2 (chat generation)
  * DistilBERT (sentiment analysis)
* **Torch**
* **Pillow (PIL)** – image handling
* **JSON** – rule-based responses

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-voice-assistant.git
cd ai-voice-assistant
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ **Important (Windows users)**
> If PyAudio fails:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Running the Assistant

```bash
python gui.py
```

Click **Ask**, speak clearly, and interact with your assistant 🎤🤖

---

## 🧾 Example `responses.json`

```json
{
  "hello": "Hi! How can I help you today?",
  "what is your name": "My name is Virtual Assistant.",
  "good morning": "Good morning! Hope you have a great day.",
  "what is the time": "I can tell you the current time."
}
```

---

## 🧪 Example Commands

* “Hello”
* “What is your name?”
* “Open Google”
* “Play music”
* “What is the time?”
* Any **free-form question** → handled by GPT-2

---

## 🚀 Improvements You Can Add

* Memory / conversation history
* Offline NLP models
* Wake-word detection
* Better intent classification (spaCy / Rasa)
* Fine-tuned LLM
* API integration (weather, news, calendar)
* Database-backed knowledge base

---

## 🛡️ Known Warnings (Safe)

* **OpenMP warning** → harmless on Windows
* **Tokenizer warnings** → informational
* **Model download logs** → normal first-time behavior

---

## 🎯 Learning Outcomes

This project demonstrates:

* Real-world Python GUI development
* Speech & audio processing
* NLP pipelines
* Hybrid AI system design (rules + ML)
* Practical debugging & model integration

---

## 👨‍💻 Author

**Michael**
Computer Science / Informatics
AI • NLP • Data Analytics • Cybersecurity

> Built as a learning-focused AI assistant with real-world extensibility.
## LICENSE 
## 📄 License
**Copyright © 2026 Michael Mirieri. All Rights Reserved.**

This project is proprietary and confidential. Unauthorized copying, distribution, or modification 
of this file or project, via any medium, is strictly prohibited.

Permission is granted for academic evaluation and recruitment viewing only.

---

Just say the word 😄

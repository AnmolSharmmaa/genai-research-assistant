
# 🧠 GenAI Research Assistant

An intelligent, voice-enabled assistant that allows users to upload documents (PDF/TXT), auto-summarize them, ask questions by text or voice, and get evaluated in a unique **Challenge Me** mode that tests logical comprehension. Designed with a modern glassmorphism UI using Streamlit.

![GenAI Research Assistant](https://cdn.prod.website-files.com/679038f47d3aba15a7876e30/682dfc3c5bce1e1a682f066b_How%20to%20Train%20GenAI%20to%20Work%20as%20Your%20Personal%20Research%20Assistant.jpg)

---

## 🚀 Features

- 📄 **Document Upload** (PDF/TXT)
- ✨ **Auto Summarization** using BART
- 💬 **Q&A Interaction** (text + voice input)
- 🧠 **Challenge Me** Mode: logic-based quiz generated from document
- 🎙️ Voice-to-text via `speech_recognition`
- 🔊 Text-to-speech via `gTTS`
- 📄 Downloadable `.docx` report of session
- 💡 Dark-themed UI with custom CSS and animated components

---

## 🧰 Tech Stack

- **Frontend**: Streamlit + Custom HTML/CSS (Glassmorphism, dark theme)
- **NLP Models**:
  - `BART` (Summarization)
  - `DistilBERT` (Q&A)
- **Voice**:
  - `speech_recognition` for voice input
  - `gTTS` for voice output
- **Backend**: Python, PyTorch, Transformers, docx
- **Others**: pdfminer, whisper (optional), re, os

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/genai-research-assistant.git
cd genai-research-assistant
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# OR Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

> ✅ Ensure your microphone is working for voice features.
> 📄 Place your background video/image inside the `static/` folder for visual enhancements.

## 🏗️ Architecture & Reasoning Flow

```text
User Uploads File ─┬─> Summarizer (BART) ─┬─> Summary Displayed
                   └─> QA Engine (DistilBERT) ─┬─> Ask Anything (text or voice)
                                              └─> Challenge Me ──> 3 Logic Qs ──> Evaluation
                                                           └─> Final Report (.docx)


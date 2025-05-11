# 🎙️ Voice-Activated GPT Assistant

This project is a simple yet powerful **voice assistant** that listens to your speech, sends your query to **OpenAI's GPT model**, and responds to you using **text-to-speech**. It combines **speech recognition**, **OpenAI GPT**, and **pyttsx3** to create a hands-free conversational experience.

---

## 🚀 Features

* 🎧 Voice input using your microphone
* 🧠 Text generation using OpenAI's GPT-3.5 model
* 🔊 Voice response using `pyttsx3` text-to-speech
* 🔁 Continuous conversation loop until you say "exit" or "quit"

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/bayojuvikas/Amazon_Alexa_Re-Engineered.git
   cd Amazon_Alexa_Re-Engineered
   ```

2. **Install dependencies**

   ```bash
   pip install openai SpeechRecognition pyttsx3 pyaudio
   ```

3. **Set your OpenAI API Key**
   You can set the API key as an environment variable:

   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

The assistant will greet you and wait for your voice input. Speak your command clearly, and the assistant will respond.

Say **"exit"** or **"quit"** to stop the program.

---

## 🧠 How It Works

1. **Listen** – Uses your microphone to capture voice.
2. **Recognize** – Converts speech to text using Google's Speech Recognition API.
3. **Respond** – Sends the recognized text to OpenAI's GPT-3.5 and generates a response.
4. **Speak** – Converts the GPT response to speech and reads it aloud.

---

## 📌 Notes

* Make sure your microphone is connected and configured properly.
* Requires a valid [OpenAI API Key](https://platform.openai.com/account/api-keys).
* Built using `gpt-3.5-turbo` (Note: API may interpret as `text-davinci-003` unless modified via chat endpoint).

---

## 📄 License

This project is open-source

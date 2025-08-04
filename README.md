# Murf-AI
30 Days of AI Voice Agents
🎤 Murf AI TTS with FastAPI
#30DaysofVoiceAgents by Murf AI

A simple text‑to‑speech web application built with FastAPI (backend) and TailwindCSS (frontend). The app takes user input text, sends it to Murf AI’s REST API, and returns an audio file that can be played directly in the browser.

📌 Features
FastAPI Backend
/tts endpoint: Accepts text, calls Murf AI /generate API, returns audio URL
/voices endpoint: Retrieves available voices from Murf AI

Frontend
Text input + “Generate Audio” button
<audio> element to play generated speech instantly
Secure API key handling with .env
API tested via Swagger UI (localhost:8000/docs)

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/murf-tts-fastapi.git
cd murf-tts-fastapi
2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install fastapi uvicorn jinja2 python-dotenv requests
4️⃣ Configure API Key
Create a .env file in the project root:
MURF_API_KEY=your_real_murf_api_key
5️⃣ Run the server
uvicorn main:app --reload

The app will be available at:
👉 http://127.0.0.1:8000 (Frontend)
👉 http://127.0.0.1:8000/docs (Swagger UI)

🌐 API Endpoints
GET /voices
Fetch all supported voices from Murf AI.

Example Response:

[
  {
    "voice_id": "en-US-Jenny",
    "language": "English (US)",
    "style": "Conversational"
  }
]
POST /tts
Generate TTS audio from given text and voice.

Request:

{
  "text": "Hello Murf AI from FastAPI!",
  "voice_id": "en-US-Jenny"
}
Response:

{
  "audioFile": "https://murf.ai/user-upload/...wav"
}

🎨 UI Preview
Responsive design built with TailwindCSS
Input field + Generate button
Audio playback with <audio> element


🏷 Tech Stack
Backend: FastAPI, Uvicorn
Frontend: HTML, TailwindCSS
API: Murf AI REST API
Environment Management: python-dotenv

Acknowledgements
Special thanks to Murf AI for the API and challenge.
Project built as part of #30DaysofVoiceAgents and #BuildwithMurf.

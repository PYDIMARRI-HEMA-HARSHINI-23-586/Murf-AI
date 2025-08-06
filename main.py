from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import os
from dotenv import load_dotenv
import uvicorn
from fastapi import File, UploadFile


# Load API key
load_dotenv()
MURF_API_KEY = os.getenv("MURF_API_KEY")

app = FastAPI()

# Static + templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Fetch available voices
@app.get("/voices")
async def get_voices():
    url = "https://api.murf.ai/v1/speech/voices"
    headers = {"api-key": MURF_API_KEY}
    response = requests.get(url, headers=headers)
    return JSONResponse(content=response.json())

# Generate TTS
@app.post("/tts")
async def generate_tts(data: dict = Body(...)):
    text = data.get("text")
    voice_id = data.get("voice_id")  # Pass from available voices
    
    url = "https://api.murf.ai/v1/speech/generate"
    headers = {
        "api-key": MURF_API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "voice_id": voice_id,
        "text": text
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code != 200:
        return JSONResponse(content={"error": "Murf API Error", "details": response.text}, status_code=response.status_code)
    
    return JSONResponse(content=response.json())
    

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    
    # Save file to /uploads folder
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    # Return file info
    file_info = {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": os.path.getsize(file_location)
    }
    
    return file_info


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

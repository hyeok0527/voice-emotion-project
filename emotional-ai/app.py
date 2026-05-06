from fastapi import FastAPI, UploadFile, File
import shutil
import os

from my_utils import extract_features
from model import predict

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    features = extract_features(file_path)
    top_emotion, result = predict(features)

    return {
        "filename": file.filename,
        "topEmotion": top_emotion,
        "result": result
    }
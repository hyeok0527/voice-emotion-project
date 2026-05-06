from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def analyze_emotion(file_path: str):
    """
    백엔드 담당자(B)의 역할에 따른 더미 데이터 반환 함수
    """
    dummy_result = {
        "filename": file_path.split("/")[-1],
        "topEmotion": "happy",
        "result": [
            {"label": "happy", "score": 0.7},
            {"label": "sad", "score": 0.2},
            {"label": "angry", "score": 0.1}
        ]
    }
    return dummy_result

# API 엔드포인트
@app.post("/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):
    result = analyze_emotion(file.filename)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

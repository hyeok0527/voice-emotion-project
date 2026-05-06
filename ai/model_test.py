import json

def analyze_emotion(file_path: str):
    """
    AI 모델 테스트를 위한 함수입니다.
    현재는 1주차 목표에 따라 더미 데이터를 반환합니다.
    """
    # 실제 모델 로드 및 추론 로직이 여기에 들어갑니다.
    # 예: model.predict(audio)
    
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

if __name__ == "__main__":
    # 독립 실행 시 테스트 코드
    test_file = "sample.wav"
    result = analyze_emotion(test_file)
    print(json.dumps(result, indent=4))

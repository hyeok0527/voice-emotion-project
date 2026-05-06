import numpy as np
from sklearn.ensemble import RandomForestClassifier

EMOTIONS = ["happy", "sad", "angry"]

model = RandomForestClassifier()

# 더미 데이터로 학습 (테스트용)
X = np.random.rand(100, 13)
y = np.random.choice(EMOTIONS, 100)
model.fit(X, y)


def predict(features):
    probs = model.predict_proba(features)[0]
    labels = model.classes_

    result = []
    for label, score in zip(labels, probs):
        result.append({
            "label": label,
            "score": float(score)
        })

    top_emotion = labels[np.argmax(probs)]

    return top_emotion, result

def predict(features):
    # 연결 테스트를 위한 가짜 결과 데이터
    top_emotion = "happy"
    result = [
        {"label": "happy", "score": 0.8},
        {"label": "sad", "score": 0.1},
        {"label": "angry", "score": 0.1}
    ]
    return top_emotion, result
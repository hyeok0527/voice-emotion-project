import joblib
import numpy as np

model = joblib.load("model.pkl")


def predict(features):
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]

    labels = model.classes_

    result = []

    for label, score in zip(labels, probabilities):
        result.append({
            "label": label,
            "score": float(score)
        })

    return prediction, result
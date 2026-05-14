import os
import numpy as np
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from my_utils import extract_features

DATASET_PATH = "dataset"

X = []
y = []

emotions = ["happy", "sad", "angry"]

for emotion in emotions:
    folder = os.path.join(DATASET_PATH, emotion)

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        features = extract_features(file_path)

        X.append(features)
        y.append(emotion)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, "model.pkl")

print("model.pkl 저장 완료")
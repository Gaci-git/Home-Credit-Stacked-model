import pickle
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/stacked_model.pkl", "rb") as f:
    model = pickle.load(f)


classes = [
    "Will pay off",
    "Faulty loan"
]


def model_predict(values):
    pred = model.predict(values)
    return classes[pred[0]]

# ✅ File: inference/tfidf_inference.py
import joblib
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier

def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/xgboost_model.pkl")
    vectorizer = joblib.load(f"{model_dir}/tfidf_vectorizer.pkl")
    return model, vectorizer

def input_fn(request_body, content_type="application/json"):
    if content_type == "application/json":
        data = json.loads(request_body)
        return data
    raise ValueError("Unsupported content type")

def predict_fn(input_data, model_and_vectorizer):
    model, vectorizer = model_and_vectorizer
    if isinstance(input_data, list):
        transformed = vectorizer.transform(input_data).toarray()
    else:
        transformed = vectorizer.transform([input_data]).toarray()
    prediction = model.predict(transformed)
    return prediction.tolist()

def output_fn(prediction, accept="application/json"):
    if accept == "application/json":
        return json.dumps({"prediction": prediction})
    raise ValueError("Unsupported accept type")

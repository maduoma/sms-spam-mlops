# scripts/preprocess.py

import os
import re
import pandas as pd
import numpy as np
import string
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# ---------------------- Constants ---------------------- #
DATA_PATH = os.path.join("data", "sms.tsv")
PROCESSED_DIR = os.path.join("data", "processed")
VECTORIZER_PATH = os.path.join(PROCESSED_DIR, "tfidf_vectorizer.pkl")
LABEL_ENCODER_PATH = os.path.join(PROCESSED_DIR, "label_encoder.pkl")

# Ensure output dir exists
os.makedirs(PROCESSED_DIR, exist_ok=True)


# ---------------------- Text Cleaning ---------------------- #
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    text = re.sub(r"\d+", "", text)  # remove digits
    text = text.strip()
    return text


# ---------------------- Main Pipeline ---------------------- #
def preprocess():
    print("[INFO] Loading dataset...")
    df = pd.read_csv(DATA_PATH, sep="\t", header=None, names=["label", "text"])
    df.dropna(inplace=True)

    print(f"[INFO] Loaded {len(df)} records.")

    # Clean text
    print("[INFO] Cleaning text...")
    df["text_clean"] = df["text"].apply(clean_text)

    # Encode labels (spam=1, ham=0)
    print("[INFO] Encoding labels...")
    label_encoder = LabelEncoder()
    df["label_encoded"] = label_encoder.fit_transform(df["label"])

    # TF-IDF Vectorization
    print("[INFO] Vectorizing text...")
    vectorizer = TfidfVectorizer(max_features=3000)
    X = vectorizer.fit_transform(df["text_clean"]).toarray()
    y = df["label_encoded"].values

    # Train/Test Split
    print("[INFO] Splitting train/test data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Save artifacts
    print("[INFO] Saving vectorizer and data splits...")
    joblib.dump(vectorizer, VECTORIZER_PATH)
    joblib.dump(label_encoder, LABEL_ENCODER_PATH)

    np.save(os.path.join(PROCESSED_DIR, "X_train.npy"), X_train)
    np.save(os.path.join(PROCESSED_DIR, "X_test.npy"), X_test)
    np.save(os.path.join(PROCESSED_DIR, "y_train.npy"), y_train)
    np.save(os.path.join(PROCESSED_DIR, "y_test.npy"), y_test)

    print("[SUCCESS] Preprocessing complete. Artifacts saved to 'data/processed/'.")


if __name__ == "__main__":
    preprocess()
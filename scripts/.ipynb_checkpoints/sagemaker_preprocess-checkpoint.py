# scripts/sagemaker_preprocess.py

import os
import pandas as pd
import numpy as np
import joblib
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    text = text.strip()
    return text

if __name__ == "__main__":
    input_path = "/opt/ml/processing/input/sms.tsv"
    output_dir = "/opt/ml/processing/output"

    df = pd.read_csv(input_path, sep="\t", header=None, names=["label", "text"])
    df["text_clean"] = df["text"].apply(clean_text)

    # Label encode
    le = LabelEncoder()
    df["label_encoded"] = le.fit_transform(df["label"])

    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=3000)
    X = vectorizer.fit_transform(df["text_clean"]).toarray()
    y = df["label_encoded"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

    # Save
    np.save(os.path.join(output_dir, "X_train.npy"), X_train)
    np.save(os.path.join(output_dir, "X_test.npy"), X_test)
    np.save(os.path.join(output_dir, "y_train.npy"), y_train)
    np.save(os.path.join(output_dir, "y_test.npy"), y_test)

    joblib.dump(vectorizer, os.path.join(output_dir, "vectorizer.pkl"))
    joblib.dump(le, os.path.join(output_dir, "label_encoder.pkl"))

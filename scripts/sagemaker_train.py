# scripts/sagemaker_train.py

import joblib
import numpy as np
import os
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

if __name__ == "__main__":
    input_dir = "/opt/ml/input/data/train"
    model_dir = "/opt/ml/model"

    # Load
    X_train = np.load(os.path.join(input_dir, "X_train.npy"))
    y_train = np.load(os.path.join(input_dir, "y_train.npy"))
    X_test = np.load(os.path.join(input_dir, "X_test.npy"))
    y_test = np.load(os.path.join(input_dir, "y_test.npy"))

    model = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=4,
        use_label_encoder=False,
        eval_metric="logloss",
        random_state=42
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, preds)
    roc_auc = roc_auc_score(y_test, probs)
    report = classification_report(y_test, preds)

    print(f"Accuracy: {acc:.4f}")
    print(f"ROC-AUC: {roc_auc:.4f}")
    print(report)

    # Save model
    joblib.dump(model, os.path.join(model_dir, "xgboost_model.pkl"))

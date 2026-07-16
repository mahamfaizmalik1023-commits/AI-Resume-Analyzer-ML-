import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from xgboost import XGBClassifier

print("=" * 60)
print("Training ATS XGBoost Model")
print("=" * 60)

# Load ATS dataset
df = pd.read_csv("datasets/ats_training_data.csv")

print("\nDataset Shape:", df.shape)

# Features
X = df[
    [
        "Semantic",
        "Skill_Match",
        "Experience_Match",
        "Education_Match",
        "Certification_Match",
    ]
]

# Target
y = df["Label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# Build Model
model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    random_state=42,
    eval_metric="logloss",
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, predictions))

# Save model
joblib.dump(model, "models/ats_xgboost_model.pkl")

print("\nATS Model Saved Successfully!")
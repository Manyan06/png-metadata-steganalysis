import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load features
df = pd.read_csv("features.csv")

# ---- Binary classification: clean vs stego ----
df["binary_label"] = df["label"].apply(lambda x: "stego" if x != "clean" else "clean")

X = df[
    ["num_meta_keys", "total_meta_len", "avg_value_len",
     "mean_entropy", "mean_ascii_ratio"]
]
y = df["binary_label"]

# Encode labels
le = LabelEncoder()
y_enc = le.fit_transform(y)

# Train model on full dataset (proof-of-concept)
model = LogisticRegression()
model.fit(X, y_enc)

# Predict on same data
y_pred = model.predict(X)

print("=== Binary Classification (Clean vs Stego) ===")
print(confusion_matrix(y_enc, y_pred))
print(classification_report(y_enc, y_pred, target_names=le.classes_))
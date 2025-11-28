import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# -------------------------------
# Feature Extraction Function
# -------------------------------
def extract_features(password):
    length = len(password)
    uppercase = len(re.findall(r"[A-Z]", password))
    lowercase = len(re.findall(r"[a-z]", password))
    digits = len(re.findall(r"[0-9]", password))
    special = len(re.findall(r"[@#$%^&*()_+!]", password))
    return [length, uppercase, lowercase, digits, special]

# -------------------------------
# Sample Dataset
# -------------------------------
passwords = [
    "abc", "password", "hello123", "Admin123", "Admin@123",
    "Pass123", "Strong@123", "Weak", "Qwerty", "Qwerty@123",
    "Hi@12", "Machine@2024", "MLproject@123"
]

strength = [
    0, 0, 1, 1, 2,
    1, 2, 0, 0, 2,
    0, 2, 2
]  
# 0 = Weak | 1 = Medium | 2 = Strong

# -------------------------------
# Create Dataset
# -------------------------------
X = [extract_features(p) for p in passwords]
y = strength

X = np.array(X)
y = np.array(y)

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Train ML Model
# -------------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# -------------------------------
# Model Accuracy
# -------------------------------
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# -------------------------------
# Password Strength Prediction
# -------------------------------
def predict_strength(password):
    features = extract_features(password)
    prediction = model.predict([features])[0]

    if prediction == 0:
        return "Weak Password"
    elif prediction == 1:
        return "Medium Password"
    else:
        return "Strong Password"

# -------------------------------
# User Input
# -------------------------------
user_password = input("Enter password: ")
print("Password Strength:", predict_strength(user_password))
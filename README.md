# Intelligent-Password-Strength-Checking-Using-Machine-Learning
🔐 Intelligent Password Strength Checker using Machine Learning

This project implements a Machine Learning–based system to accurately measure password strength.  
Instead of using simple rule-based checks (length, special characters, digits), this system extracts  
advanced features such as entropy, character distribution, repetition patterns, and predicts  
password strength as *Weak, **Moderate, or **Strong*.

This project is developed as part of the *Fundamentals of AI and ML* course and follows  
VITyarthi "Build Your Own Project" guidelines.

---

## 📘 Project Overview

Traditional password strength meters only check for symbols or length. They often fail to estimate  
actual password security because they do not consider deeper patterns such as entropy and  
dictionary-based weakness.

This project uses machine learning to analyze unique password features and classify  
strength with better accuracy.

---

## 🎯 Key Features

### ✔ Functional Features
- User inputs password
- System extracts advanced features:
  - Length
  - Uppercase/Lowercase/Digit/Symbol counts
  - Shannon entropy
  - Repetition pattern score
- ML model predicts:
  - *Weak*
  - *Moderate*
  - *Strong*
- Suggests improvements for weak passwords

### ✔ Technical Features
- Random Forest Classifier
- Custom password feature extraction
- Modular Python code (features.py, train.py, predict.py)
- Model saved using joblib

---

## 🧠 Technologies Used

- Python 3.x  
- Scikit-learn  
- Pandas  
- Joblib  
- Math, Regex (re module)  

---

## 📁 Dataset Format

The dataset contains:

password,length,upper,lower,digits,symbols,entropy,repetition_score,label pass123,7,0,4,3,0,22.1,1,Weak P@ssw0rd123!,12,1,5,3,3,54.8,1,Strong admin,5,0,5,0,0,14.2,5,Weak ...

---

## 📂 Project Structure

Password-Strength-Checker-ML/ │ ├── passwords.csv ├── model.pkl │ ├── features.py ├── train.py ├── predict.py │ └── README.md

---

## 🚀 How to Run the Project

### 1️⃣ Install required libraries
```bash
pip install scikit-learn pandas joblib

2️⃣ Train the Model

python train.py

Output example:

precision    recall  f1-score   support
Weak             0.94       0.95      0.94
Moderate         0.92       0.90      0.91
Strong           0.96       0.97      0.96

Model saved as model.pkl

3️⃣ Predict Password Strength

python predict.py

Sample output:

Enter password: P@ssw0rd123!
Password Strength: Strong


---

🧪 Testing

Test with various combinations:

Only digits

Only letters

Mixed characters

Very short / very long passwords


Compare ML predictions with entropy-based rules



---

⚠ Limitations

Quality depends on dataset richness

Keyboard pattern detection limited

No dictionary word blacklist yet



---

🔮 Future Improvements

Add deep learning (LSTM) for sequence analysis

Real-time strength meter (web-based)

Dictionary word detection

Multi-language password analysis



---

🙏 Acknowledgment

This project follows the VITyarthi Build Your Own Project Guidelines.

---

# ✅ *ALL DESIGN DIAGRAMS (Text-Based for Report/PPT)*  

You can *copy these into your report* OR  
I can generate image versions (PNG) if you want — just tell me *“Give PNG diagrams”*

---

# *📌 1. Use Case Diagram (Text Format)*

+-------------------+
        |      USER         |
        +---------+---------+
                  |
                  v
      +-----------+-----------+
      |  Submit Password       |
      +-----------+-----------+
                  |
                  v
    +-------------+-------------+
    | Get Strength Prediction   |
    +-------------+-------------+
                  |
                  v
    +-------------+-------------+
    | View Suggestions           |
    +----------------------------+

---

# *📌 2. Workflow Diagram*

Start | v User Inputs Password | v Feature Extraction | v ML Model Prediction | v Strength Category Displayed | v Suggestions Provided | v End

---

# *📌 3. Sequence Diagram*

User → System: Enter password System → FeatureExtractor: Extract features FeatureExtractor → ML Model: Send features ML Model → System: Return prediction System → User: Display Weak/Moderate/Strong

---

# *📌 4. System Architecture Diagram*

+----------------------+
        |      User Input      |
        +----------+-----------+
                   |
                   v
        +----------+-----------+
        |  Feature Extraction   |
        | (entropy, patterns)   |
        +----------+-----------+
                   |
                   v
        +----------+-----------+
        |   ML Model (RF)      |
        +----------+-----------+
                   |
                   v
        +----------+-----------+
        | Output + Suggestions |
        +----------------------+

---

# *📌 5. Class Diagram*

+--------------------------+ |     FeatureExtractor     | +--------------------------+ | extract_features()       | | compute_entropy()        | | repetition_score()       | +--------------------------+

+--------------------------+ |      ModelTrainer        | +--------------------------+ | train_model()            | | save_model()             | +--------------------------+

+--------------------------+ |        Predictor         | +--------------------------+ | load_model()             | | predict_strength()       | +--------------------------+

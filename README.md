# Save README.md file
readme_content = """
# 🏦 Loan Approval Prediction App

A complete **End-to-End Machine Learning Project** using the [Loan Prediction Dataset (Kaggle)](https://www.kaggle.com/datasets/ninzaami/loan-predication) to predict whether a loan application will be approved or rejected.

Built with:
- **Python** (Pandas, NumPy, Scikit-learn)
- **Streamlit** (for interactive web app)
- **Matplotlib & Seaborn** (for EDA visualizations)
- **Joblib** (for saving/loading model artifacts)

---

## 📌 Project Overview

This project walks through the **full ML lifecycle**:

1. **Data Loading & Inspection**  
2. **Data Cleaning** (missing values, data types)  
3. **EDA** (countplots, histograms, correlations)  
4. **Feature Encoding** (binary mapping, one-hot encoding)  
5. **Feature Scaling** (only continuous numeric columns)  
6. **Train/Test Split**  
7. **Model Training** (Logistic Regression, Random Forest)  
8. **Evaluation** (Accuracy, Precision, Recall, F1-score, ROC-AUC, Confusion Matrix)  
9. **Hyperparameter Tuning** (GridSearchCV)  
10. **Saving Artifacts** (model, scaler, feature columns, numeric columns)  
11. **Streamlit App** (form → prediction: “Loan Approved” or “Loan Rejected”)  
12. **Project Documentation & GitHub Setup**  

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **Libraries:**
  - pandas, numpy
  - scikit-learn
  - matplotlib, seaborn
  - streamlit
  - joblib
- **Environment:** Virtualenv (.venv)

---

## 📂 Project Structure

loan-approval/
│
├── data/
│   ├── raw/                 # Original dataset (CSV from Kaggle)
│   └── processed/           # Cleaned/transformed data
│
├── models/                  # Saved model + scaler + metadata
│   ├── loan_rf_model.joblib
│   ├── scaler.joblib
│   ├── feature_columns.joblib
│   └── num_cols.joblib
│
├── notebooks/               # Jupyter Notebooks
│   └── 01_eda_and_baseline.ipynb
│
├── app/                     # Streamlit app
│   └── app.py
│
├── requirements.txt         # Dependencies
└── README.md                # Project documentation

---

## 🚀 How to Run

### 1️⃣ Clone the repo
git clone <your-repo-link>
cd loan-approval

### 2️⃣ Create & activate virtual environment
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1   # Windows PowerShell
# or
source .venv/bin/activate      # macOS/Linux

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the Streamlit app
streamlit run app/app.py

---

## 📊 Model Details

- **Algorithm:** Random Forest Classifier (tuned with GridSearchCV)
- **Performance Metrics:**
  - Accuracy: ~0.82 (varies depending on random state & split)
  - Precision/Recall balanced for target class
- **Feature Importance:** Credit_History, LoanAmount, ApplicantIncome have high influence

---

## ⚠️ Challenges & Solutions

### 1. Feature Name Mismatch Between Training & App
- Dropped ID columns before training.
- Used explicit binary mapping for binary features.
- One-hot encoded only Property_Area with drop_first=True.
- Saved feature_columns.joblib to ensure exact match.

### 2. Wrong Columns Being Scaled
- Created num_cols list (only continuous numeric columns).
- Saved to num_cols.joblib.
- App now loads num_cols and scales only those.

### 3. Version Mismatch Between Notebook & Streamlit Environment
- Checked training sklearn version (1.2.2) in notebook.
- Installed same version in Streamlit environment.
- Pinned versions in requirements.txt.

### 4. Encoding Consistency Between Train & Predict
- Converted "3+" to int(3) in both training and app.
- Applied same mapping logic in both notebook and app.

---

## 🎯 What We Achieved

- ✅ Clean, modular Jupyter Notebook for data prep, EDA, modeling.
- ✅ Proper artifact saving (model, scaler, column lists).
- ✅ Fully working Streamlit app with aligned preprocessing.
- ✅ Version control & dependency management to avoid runtime mismatches.
- ✅ Documented common pitfalls & how we fixed them.

---

## 🧪 Example Test Inputs

| Gender | Married | Dependents | Education     | Self Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term | Credit_History | Property_Area |
|--------|---------|------------|---------------|---------------|-----------------|-------------------|------------|------------------|----------------|---------------|
| Male   | Yes     | 0          | Graduate      | No            | 8000            | 2000              | 120        | 360              | 1              | Urban         |
| Female | No      | 2          | Not Graduate  | Yes           | 2500            | 0                 | 180        | 360              | 0              | Rural         |
| Male   | Yes     | 1          | Graduate      | No            | 4000            | 1500              | 150        | 180              | 1              | Semiurban     |

---

## 📜 License
This project is for educational purposes.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md file created.")

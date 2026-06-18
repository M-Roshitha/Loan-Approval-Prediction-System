import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("../data/train.csv")

if "Loan_ID" in df.columns:
    df.drop("Loan_ID", axis=1, inplace=True)

for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

le = LabelEncoder()

for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        df[col] = le.fit_transform(df[col])
        
df = pd.get_dummies(
    df,
    columns=["Property_Area"],
    drop_first=True
)

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

os.makedirs("../models", exist_ok=True)

joblib.dump(model, "../models/loan_model.joblib")

print("Model trained successfully!")
import streamlit as st
import pandas as pd
import joblib
import os

# ---------- Paths ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "models"))

# ---------- Load Model ----------
model = joblib.load(os.path.join(MODELS_DIR, "loan_model.joblib"))

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Approval Prediction System")
st.write("Enter applicant details below and click Predict.")

# ---------- Input Form ----------
with st.form("loan_form"):

    Gender = st.selectbox("Gender", ["Male", "Female"])

    Married = st.selectbox("Married", ["No", "Yes"])

    Dependents = st.selectbox(
        "Dependents",
        ["0", "1", "2", "3+"]
    )

    Education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    Self_Employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    ApplicantIncome = st.number_input(
        "Applicant Income",
        min_value=0,
        value=5000
    )

    CoapplicantIncome = st.number_input(
        "Coapplicant Income",
        min_value=0,
        value=0
    )

    LoanAmount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=120
    )

    Loan_Amount_Term = st.number_input(
        "Loan Amount Term",
        min_value=0,
        value=360
    )

    Credit_History = st.selectbox(
        "Credit History",
        [1, 0]
    )

    Property_Area = st.selectbox(
        "Property Area",
        ["Rural", "Semiurban", "Urban"]
    )

    submitted = st.form_submit_button("Predict")

# ---------- Prediction ----------
if submitted:

    # Same encoding used during training
    gender_map = {"Male": 1, "Female": 0}
    married_map = {"Yes": 1, "No": 0}
    education_map = {"Graduate": 1, "Not Graduate": 0}
    self_map = {"Yes": 1, "No": 0}
    area_map = {
        "Rural": 0,
        "Semiurban": 1,
        "Urban": 2
    }

    dep = 3 if Dependents == "3+" else int(Dependents)

    input_data = pd.DataFrame([{
        "Gender": gender_map[Gender],
        "Married": married_map[Married],
        "Dependents": dep,
        "Education": education_map[Education],
        "Self_Employed": self_map[Self_Employed],
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Property_Area_1": 1 if area_map[Property_Area] == 1 else 0,
        "Property_Area_2": 1 if area_map[Property_Area] == 2 else 0
    }])

    try:

        prediction = model.predict(input_data)[0]

        try:
            probability = model.predict_proba(input_data)[0][1]
        except:
            probability = None

        if prediction == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

        if probability is not None:
            st.info(
                f"Approval Probability: {probability:.2%}"
            )

    except Exception as e:
        st.error(str(e))
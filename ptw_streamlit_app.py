
import streamlit as st
import pandas as pd
import joblib
from io import BytesIO

from scripts.streamlit_data_integration import render_data_integration_tab

st.set_page_config(page_title="PTW Win Probability Tool", layout="wide")
st.title("Price-to-Win Intelligence Suite")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Scenario Comparison",
    "Salary Estimator",
    "Live PTW Calculator",
    "Data Integration"
])

if page == "Scenario Comparison":
    st.subheader("Scenario-Based Rate Modeling")
    file = st.file_uploader("Upload Excel File", type=["xlsx"])
    if file:
        df = pd.read_excel(file)
        st.dataframe(df, use_container_width=True)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='PTW_Scenarios')
        st.download_button("Download Scenario Report", output.getvalue(), file_name="PTW_Scenario_Export.xlsx")

elif page == "Salary Estimator":
    st.header("AI-Powered Salary Estimator")
    try:
        model, feature_cols = joblib.load("salary_estimator_model.pkl")
        job_title = st.selectbox("Job Title", ["Logistics Analyst IV", "Program Manager", "Management Analyst",
            "Supply Technician", "Medical LNO", "Administrative Assistant", "Database Analyst", "Help Desk Specialist"])
        education = st.selectbox("Education Requirement", ["High School", "Associate's", "Bachelor's"])
        experience = st.slider("Years of Experience", min_value=0, max_value=30, value=5)
        clearance = st.selectbox("Clearance Required", ["None", "Secret"])
        location = st.selectbox("Location", ["Fort Bragg, NC", "Frederick, MD", "Remote", "Fort Carson, CO",
            "Germany", "Fort Detrick, MD", "JB Elmendorf–Richardson, AK", "Ft. Cavazos, TX"])
        input_df = pd.DataFrame([{
            "Job Title": job_title,
            "Education Requirement": education,
            "Years of Experience": experience,
            "Clearance Required": clearance,
            "Location": location
        }])
        input_encoded = pd.get_dummies(input_df).reindex(columns=feature_cols, fill_value=0)
        estimated_salary = model.predict(input_encoded)[0]
        st.success(f"Estimated Competitive Base Salary: ${estimated_salary:,.2f}")
    except Exception as e:
        st.error("Model could not be loaded or input structure mismatch.")

elif page == "Live PTW Calculator":
    st.subheader("Live PTW Rate Evaluation")
    proposed_rate = st.number_input("Proposed Bill Rate ($/hr)", value=100.00)
    evaluation_type = st.selectbox("Evaluation Type", ["LPTA", "Best Value"])
    intensity = st.selectbox("Job Intensity", ["High", "Medium", "Low"])
    specialized = st.selectbox("Specialized/Unique Requirement", ["Yes", "No"])
    trend = st.selectbox("Political/Government Trend", ["Expansionary (+0.03)", "Neutral (0)", "Contractionary (-0.03)"])
    mod = 1 + (0.03 if trend.startswith("Expansionary") else -0.03 if trend.startswith("Contractionary") else 0)
    spec_mod = 1.05 if specialized == "Yes" else 1
    int_mod = 1.1 if intensity == "High" else 1.05 if intensity == "Medium" else 1
    adjusted_rate = proposed_rate * mod * spec_mod * int_mod
    win_prob = 0.85 if evaluation_type == "LPTA" and intensity == "High" else                0.75 if evaluation_type == "LPTA" and intensity == "Medium" else                0.65 if evaluation_type == "LPTA" else                0.65 if intensity == "High" else 0.55 if intensity == "Medium" else 0.45
    st.metric(label="Adjusted Rate ($/hr)", value=f"${adjusted_rate:.2f}")
    st.metric(label="Win Probability (%)", value=f"{int(win_prob * 100)}%")

elif page == "Data Integration":
    render_data_integration_tab()

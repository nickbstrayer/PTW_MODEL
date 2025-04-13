import streamlit as st
import pandas as pd
import joblib
from io import BytesIO

# Import tabs
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.streamlit_auth import render_auth_page  # ✅ NEW: User Login tab

# Set page configuration
st.set_page_config(page_title="PTW Win Probability Tool", layout="wide")
st.title("Price-to-Win Intelligence Suite")

# Sidebar menu
selection = st.sidebar.radio("Go to", [
    "Scenario Comparison",
    "Salary Estimator",
    "Live PTW Calculator",
    "Data Integration",
    "SAM Vendor Lookup",
    "User Login"  # ✅ NEW
])

# Route to correct page
if selection == "Scenario Comparison":
    st.subheader("Scenario Comparison (Coming Soon)")
    st.info("This section is under development.")

elif selection == "Salary Estimator":
    st.subheader("Salary Estimator (Coming Soon)")
    st.info("This section is under development.")

elif selection == "Live PTW Calculator":
    st.subheader("Live PTW Calculator (Coming Soon)")
    st.info("This section is under development.")

elif selection == "Data Integration":
    render_data_integration_tab()

elif selection == "SAM Vendor Lookup":
    render_sam_vendor_lookup_tab()

elif selection == "User Login":  # ✅ NEW
    render_auth_page()

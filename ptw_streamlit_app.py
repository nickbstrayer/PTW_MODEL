import streamlit as st

# Page config
st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    page_icon="📊",
    layout="wide",
)

# Tabs (import functions)
from Scripts.streamlit_auth import render_auth_page
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab

# Optional future tabs
# from Scripts.scenario_comparison import render_scenario_comparison_tab
# from Scripts.salary_estimator import render_salary_estimator_tab
# from Scripts.ptw_calculator import render_ptw_calculator_tab

# ----------------------------
# Session State Defaults
# ----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None
if "role" not in st.session_state:
    st.session_state.role = None

# ----------------------------
# Main App Navigation
# ----------------------------
def main_app():
    st.title("💼 Price-to-Win Intelligence Suite")

    menu = [
        "Scenario Comparison",
        "Salary Estimator",
        "Live PTW Calculator",
        "Data Integration",
        "SAM Vendor Lookup",
        "Manage Subscription",
        "User Login",
    ]

    if st.session_state.role == "admin":
        menu.append("Admin Dashboard")

    choice = st.sidebar.radio("Go to", menu)

    if choice == "Scenario Comparison":
        if st.session_state.authenticated:
            st.subheader("Scenario Comparison")
            st.info("This section will show PTW scenario analysis.")
        else:
            st.warning("⛔ Please log in to access Scenario Comparison.")

    elif choice == "Salary Estimator":
        if st.session_state.authenticated:
            st.subheader("Salary Estimator")
            st.info("This section will include salary trend predictions.")
        else:
            st.warning("⛔ Please log in to access Salary Estimator.")

    elif choice == "Live PTW Calculator":
        if st.session_state.authenticated:
            st.subheader("Live PTW Calculator")
            st.info("This section will provide a real-time PTW tool.")
        else:
            st.warning("⛔ Please log in to access PTW Calculator.")

    elif choice == "Data Integration":
        if st.session_state.authenticated:
            render_data_integration_tab()
        else:
            st.warning("⛔ Please log in to access Data Integration.")

    elif choice == "SAM Vendor Lookup":
        if st.session_state.authenticated:
            render_sam_vendor_lookup_tab()
        else:
            st.warning("⛔ Please log in to access SAM Lookup.")

    elif choice == "Manage Subscription":
        if st.session_state.authenticated:
            render_stripe_billing_tab()
        else:
            st.warning("⛔ Please log in to access billing.")

    elif choice == "User Login":
        render_auth_page()

    elif choice == "Admin Dashboard":
        if st.session_state.role == "admin":
            render_admin_dashboard_tab()
        else:
            st.warning("⛔ Admin access only.")

# ----------------------------
# Start App
# ----------------------------
main_app()

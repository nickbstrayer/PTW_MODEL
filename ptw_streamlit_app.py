import streamlit as st
from Scripts.streamlit_auth import render_auth_page
from Scripts.admin_dashboard import render_admin_dashboard_tab
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab

# Optional: Example placeholders if needed
def render_salary_estimator_tab():
    st.title("Salary Estimator")
    st.info("Coming soon...")

def render_ptw_calculator_tab():
    st.title("Live PTW Calculator")
    st.info("Coming soon...")

def render_scenario_comparison_tab():
    st.title("Scenario Comparison")
    st.info("Coming soon...")

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("Go to")

    tabs = {}

    if st.session_state.get("is_authenticated"):
        user_role = st.session_state.get("user_role", "user")

        tabs["Scenario Comparison"] = render_scenario_comparison_tab
        tabs["Salary Estimator"] = render_salary_estimator_tab
        tabs["Live PTW Calculator"] = render_ptw_calculator_tab
        tabs["Data Integration"] = render_data_integration_tab
        tabs["SAM Vendor Lookup"] = render_sam_vendor_lookup_tab
        tabs["Manage Subscription"] = render_stripe_billing_tab

        if user_role == "admin":
            tabs["Admin Dashboard"] = render_admin_dashboard_tab

        tabs["User Login"] = render_auth_page
    else:
        tabs["User Login"] = render_auth_page

    selected = st.sidebar.radio("Go to", list(tabs.keys()))
    return tabs[selected]

# App Entry Point
def main_app():
    st.set_page_config(
        page_title="Price-to-Win Intelligence Suite",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    if "is_authenticated" not in st.session_state:
        st.session_state.is_authenticated = False
        st.session_state.user_role = None
        st.session_state.current_user = None

    selected_tab = sidebar_navigation()
    selected_tab()

if __name__ == "__main__":
    main_app()

# ptw_streamlit_app.py
import streamlit as st
from Scripts.streamlit_auth import render_auth_page
from Scripts.admin_dashboard import render_admin_dashboard_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.sam_api_integration import render_scenario_tab
from Scripts.gsa_fpds_data_pull import render_salary_tab

st.set_page_config(page_title="Price-to-Win Intelligence Suite", layout="wide")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_email = ''

def main_app():
    st.title("Price-to-Win Intelligence Suite")

    tabs = [
        "Scenario Comparison",
        "Salary Estimator",
        "Live PTW Calculator",
        "Data Integration",
        "SAM Vendor Lookup",
        "Manage Subscription",
        "Admin Dashboard",
        "User Login"
    ]

    selected_tab = st.sidebar.radio("Go to", tabs, index=tabs.index("User Login"))

    if st.session_state.authenticated:
        st.sidebar.success(f"Logged in as {st.session_state.user_email}")
        if st.sidebar.button("Logout"):
            if st.sidebar.checkbox("Confirm Logout"):
                st.session_state.authenticated = False
                st.session_state.user_email = ''
                st.experimental_rerun()

    if selected_tab == "Scenario Comparison":
        if st.session_state.authenticated:
            render_scenario_tab()
        else:
            st.warning("🚫 Please log in to access Scenario Comparison.")

    elif selected_tab == "Salary Estimator":
        if st.session_state.authenticated:
            render_salary_tab()
        else:
            st.warning("🚫 Please log in to access Salary Estimator.")

    elif selected_tab == "Live PTW Calculator":
        st.info("🔧 Live PTW Calculator coming soon.")

    elif selected_tab == "Data Integration":
        if st.session_state.authenticated:
            render_data_integration_tab()
        else:
            st.warning("🚫 Please log in to access Data Integration.")

    elif selected_tab == "SAM Vendor Lookup":
        if st.session_state.authenticated:
            render_sam_vendor_lookup_tab()
        else:
            st.warning("🚫 Please log in to access SAM Vendor Lookup.")

    elif selected_tab == "Manage Subscription":
        if st.session_state.authenticated:
            render_stripe_billing_tab()
        else:
            st.warning("🚫 Please log in to access subscription settings.")

    elif selected_tab == "Admin Dashboard":
        if st.session_state.authenticated and st.session_state.user_email == "admin":
            render_admin_dashboard_tab()
        else:
            st.warning("🚫 Admin access only.")

    elif selected_tab == "User Login":
        render_auth_page()

if __name__ == "__main__":
    main_app()

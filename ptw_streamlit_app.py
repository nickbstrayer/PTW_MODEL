import streamlit as st
from Scripts.streamlit_auth import render_auth_page, logout
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab

# Set page config
st.set_page_config(page_title="Price-to-Win Intelligence Suite", layout="wide")

# Session state initialization
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = ""

# Sidebar Navigation
menu_options = [
    "Scenario Comparison",
    "Salary Estimator",
    "Live PTW Calculator",
    "Data Integration",
    "SAM Vendor Lookup",
    "Manage Subscription",
    "Admin Dashboard",
    "User Login"
]

st.sidebar.title("Go to")
selection = st.sidebar.radio("", menu_options)

# Main App Container
st.title("💼 Price-to-Win Intelligence Suite")

# Authenticated Sections
if selection == "User Login":
    render_auth_page()
    if st.session_state.authenticated:
        st.sidebar.success(f"Welcome, {st.session_state.username}")
        if st.sidebar.button("🚪 Logout"):
            if st.sidebar.confirm("Are you sure you want to logout?"):
                logout()
                st.rerun()
else:
    if not st.session_state.authenticated:
        st.warning(f"🚫 Please log in to access {selection}.")
    else:
        if selection == "Scenario Comparison":
            st.subheader("Scenario Comparison")
            st.info("Placeholder: Add scenario comparison UI here.")

        elif selection == "Salary Estimator":
            st.subheader("Salary Estimator")
            st.info("Placeholder: Add salary estimator model here.")

        elif selection == "Live PTW Calculator":
            st.subheader("Live PTW Calculator")
            st.info("Placeholder: Add calculator model here.")

        elif selection == "Data Integration":
            render_data_integration_tab()

        elif selection == "SAM Vendor Lookup":
            render_sam_vendor_lookup_tab()

        elif selection == "Manage Subscription":
            render_stripe_billing_tab()

        elif selection == "Admin Dashboard":
            if st.session_state.role == "admin":
                render_admin_dashboard_tab()
            else:
                st.error("You are not authorized to view this page.")

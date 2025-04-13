import streamlit as st
from Scripts.streamlit_auth import render_auth_page
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab

# Optional future imports
# from Scripts.scenario_comparison import render_scenario_comparison_tab
# from Scripts.salary_estimator import render_salary_estimator_tab
# from Scripts.ptw_calculator import render_ptw_calculator_tab

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Session State Initialization
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "User Login"

# -----------------------------
# Main Navigation UI
# -----------------------------
def main_app():
    st.title("Price-to-Win Intelligence Suite")

    menu_options = [
        "Scenario Comparison",
        "Salary Estimator",
        "Live PTW Calculator",
        "Data Integration",
        "SAM Vendor Lookup",
        "Manage Subscription",
        "User Login"
    ]

    if st.session_state.user_email == "admin":
        menu_options.insert(-1, "Admin Dashboard")

    selected = st.radio("Go to", menu_options, index=menu_options.index(st.session_state.active_tab))

    st.session_state.active_tab = selected

    if not st.session_state.logged_in and selected != "User Login":
        st.warning(f"🚫 Please log in to access {selected}.")
        return

    # -----------------------------
    # Render Page Based on Selection
    # -----------------------------
    if selected == "Scenario Comparison":
        st.info("Scenario Comparison will go here.")
        # render_scenario_comparison_tab()

    elif selected == "Salary Estimator":
        st.info("Salary Estimator will go here.")
        # render_salary_estimator_tab()

    elif selected == "Live PTW Calculator":
        st.info("PTW Calculator will go here.")
        # render_ptw_calculator_tab()

    elif selected == "Data Integration":
        render_data_integration_tab()

    elif selected == "SAM Vendor Lookup":
        render_sam_vendor_lookup_tab()

    elif selected == "Manage Subscription":
        render_stripe_billing_tab()

    elif selected == "Admin Dashboard":
        render_admin_dashboard_tab()

    elif selected == "User Login":
        render_auth_page()

# -----------------------------
# Launch App
# -----------------------------
main_app()

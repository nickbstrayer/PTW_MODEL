import streamlit as st

# Tabs
from Scripts.streamlit_auth import render_auth_page, initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab

# Optional: Future tabs
# from Scripts.salary_estimator import render_salary_estimator_tab
# from Scripts.ptw_scenario_comparison import render_scenario_comparison_tab

st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    layout="wide",
    page_icon="📊"
)

st.markdown("""
    <style>
    .main-container {
        padding: 2rem;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin-bottom: 2rem;
    }
    .stRadio > label {
        font-weight: 600;
        font-size: 1rem;
    }
    .block-container {
        padding-top: 1rem;
        max-width: 95%;
    }
    .stButton>button {
        border-radius: 8px;
        background-color: #1f77b4;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
    }
    .stButton>button:hover {
        background-color: #135d91;
        color: white;
    }
    .sidebar-title {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #1f77b4;
    }
    .sidebar-item {
        font-size: 1rem;
        margin: 0.5rem 0;
    }
    .user-profile {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    .user-profile img {
        border-radius: 50%;
        width: 40px;
        height: 40px;
        margin-right: 10px;
    }
    .user-details {
        font-size: 0.9rem;
    }
    @media (max-width: 768px) {
        .main-container {
            padding: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

def main_app():
    initialize_session_state()

    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_placeholder.png", width=120)
        st.markdown("<div class='sidebar-title'>📘 Navigation</div>", unsafe_allow_html=True)

        if st.session_state.is_authenticated:
            # Profile image upload
            uploaded_image = st.file_uploader("Upload Profile Image", type=["png", "jpg", "jpeg"])
            if uploaded_image:
                st.session_state["profile_image"] = uploaded_image

            # Use uploaded image if available, else fallback
            if "profile_image" in st.session_state and st.session_state["profile_image"] is not None:
                image_bytes = st.session_state["profile_image"].getvalue()
                st.image(image_bytes, width=40)
            else:
                st.image("https://avatars.githubusercontent.com/u/9919?s=40&v=4", width=40)

            # User info
            st.markdown(f"""
                <div class='user-details'>
                    <strong>User:</strong> {st.session_state.username}<br>
                    <strong>Role:</strong> {st.session_state.user_role.title()}
                </div>
            """, unsafe_allow_html=True)

        tabs = [
            "📈 Data Integration",
            "🔍 SAM Vendor Lookup",
            "💳 Manage Subscription",
            "🛠️ Admin Dashboard",
            "🔐 User Login",
        ]
        selected_tab = st.radio("", tabs, label_visibility="collapsed")

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("📊 Price-to-Win Intelligence Suite")

    # Clean routing
    if selected_tab.endswith("Data Integration"):
        if st.session_state.is_authenticated:
            render_data_integration_tab()
        else:
            st.warning("🔒 Please log in to access Data Integration.")

    elif selected_tab.endswith("SAM Vendor Lookup"):
        if st.session_state.is_authenticated:
            render_sam_vendor_lookup_tab()
        else:
            st.warning("🔒 Please log in to access SAM Vendor Lookup.")

    elif selected_tab.endswith("Manage Subscription"):
        if st.session_state.is_authenticated:
            render_stripe_billing_tab()
        else:
            st.warning("🔒 Please log in to manage your subscription.")

    elif selected_tab.endswith("Admin Dashboard"):
        if st.session_state.is_authenticated and st.session_state.user_role == "admin":
            render_admin_dashboard_tab()
        elif st.session_state.is_authenticated:
            st.warning("⚠️ Admin access required.")
        else:
            st.warning("🔒 Please log in as admin to access this tab.")

    elif selected_tab.endswith("User Login"):
        render_auth_page()

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main_app()

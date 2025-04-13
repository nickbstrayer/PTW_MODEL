import streamlit as st
from Scripts.streamlit_auth import render_auth_page, initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab
import streamlit.components.v1 as components

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
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    }
    .block-container {
        padding-top: 2rem;
        max-width: 95%;
    }
    .stButton>button {
        border-radius: 8px;
        background-color: #1f4e79;
        color: white;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.6rem 1.4rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #163b5f;
    }
    .sidebar-title {
        font-size: 1.2rem;
        font-weight: 700;
        margin: 1rem 0;
        color: #1f4e79;
    }
    .user-profile {
        display: flex;
        align-items: center;
        margin-top: 1rem;
        padding: 0.5rem;
        background-color: #eef3f7;
        border-radius: 10px;
    }
    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-right: 0.75rem;
    }
    .user-info {
        font-weight: 500;
        font-size: 0.9rem;
        color: #333;
    }
    .animated-header {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

def render_landing_page():
    st.markdown("""
    <div class='animated-header'>
        <h2>Welcome to the Price-to-Win Intelligence Suite</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        The PTW Intelligence Suite helps federal contractors make data-driven decisions with real-time insights
        from government procurement databases. Here's what you can do:

        - 🔍 Perform vendor lookups using SAM.gov data.
        - 📊 Integrate and analyze FPDS and GSA CALC data.
        - 💳 Manage your subscription and account.
        - 🛠️ Admins can manage users and monitor performance.

        ### How to Use:
        1. Use the login panel to sign in or register.
        2. After logging in, navigate the sidebar to explore features.
        3. Contact support for any access or technical issues.

        ⚠️ **Disclaimer:** This application provides data aggregation and visualization for informational purposes only.
        Always validate results with official government sources.
    """)

def main_app():
    initialize_session_state()

    if not st.session_state.get("is_authenticated"):
        render_auth_page()
        return

    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_placeholder.png", width=140)
        st.markdown("<div class='sidebar-title'>📘 Navigation</div>", unsafe_allow_html=True)

        tabs = [
            "🏠 Home",
            "📈 Data Integration",
            "🔍 SAM Vendor Lookup",
            "💳 Manage Subscription",
            "🛠️ Admin Dashboard",
            "🔐 Logout",
        ]
        selected_tab = st.radio("", tabs, label_visibility="collapsed")

        st.markdown("""
            <div class='user-profile'>
                <img src='https://ui-avatars.com/api/?name={}&background=1f4e79&color=ffffff' class='user-avatar'>
                <div class='user-info'>
                    Logged in as <strong>{}</strong><br>
                    Role: <em>{}</em>
                </div>
            </div>
        """.format(
            st.session_state.get("login_email", "User"),
            st.session_state.get("login_email", "User"),
            st.session_state.get("user_role", "member")
        ), unsafe_allow_html=True)

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("📊 Price-to-Win Intelligence Suite")

    if selected_tab.endswith("Home"):
        render_landing_page()

    elif selected_tab.endswith("Data Integration"):
        render_data_integration_tab()

    elif selected_tab.endswith("SAM Vendor Lookup"):
        render_sam_vendor_lookup_tab()

    elif selected_tab.endswith("Manage Subscription"):
        render_stripe_billing_tab()

    elif selected_tab.endswith("Admin Dashboard"):
        if st.session_state.get("user_role") == "admin":
            render_admin_dashboard_tab()
        else:
            st.warning("⚠️ Admin access required.")

    elif selected_tab.endswith("Logout"):
        if st.button("Confirm Logout"):
            st.session_state.is_authenticated = False
            st.session_state.login_email = None
            st.session_state.user_role = None
            st.success("✅ Logged out successfully. Please refresh.")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main_app()

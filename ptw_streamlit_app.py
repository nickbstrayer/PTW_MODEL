import streamlit as st
from Scripts.streamlit_auth import render_auth_page, initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab

st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    layout="wide",
    page_icon="📊"
)

# Inject modern UI styling
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding: 2rem 3rem;
        background: #f9fafb;
    }
    .stApp header { display: none; }
    .stApp footer { display: none; }
    .stButton > button {
        background-color: #0a2540;
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #11365e;
    }
    .main-card {
        background-color: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.07);
        margin-top: 1rem;
    }
    .avatar {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    .avatar img {
        width: 48px;
        height: 48px;
        border-radius: 50%;
    }
    .avatar .info {
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def main_app():
    initialize_session_state()

    with st.sidebar:
        st.markdown("<h2 style='margin-bottom: 1rem;'>📘 PTW Intelligence Suite</h2>", unsafe_allow_html=True)
        if st.session_state.is_authenticated:
            st.markdown(f"""
            <div class='avatar'>
                <img src="https://api.dicebear.com/7.x/initials/svg?seed={st.session_state.login_email}" />
                <div class='info'>
                    <strong>{st.session_state.login_email}</strong><br>
                    <small>{st.session_state.user_role.title()} Account</small>
                </div>
            </div>
            """, unsafe_allow_html=True)

        tabs = [
            "📈 Data Integration",
            "🔍 SAM Vendor Lookup",
            "💳 Manage Subscription",
            "🛠️ Admin Dashboard",
            "🔐 User Login"
        ]
        selected_tab = st.radio("Navigation", tabs)

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.title("📊 Price-to-Win Intelligence Suite")

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

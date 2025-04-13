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

def render_landing_page():
    st.markdown("""
        <style>
        .top-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 2rem;
            background-color: #0f1e45;
            color: white;
        }
        .nav-links a {
            margin-left: 1.5rem;
            color: white;
            text-decoration: none;
            font-weight: 500;
        }
        .hero {
            display: grid;
            grid-template-columns: 1fr 1fr;
            padding: 3rem 2rem;
            background-color: #f8f9fb;
            min-height: 550px;
        }
        .hero-text {
            max-width: 600px;
        }
        .hero h1 {
            font-size: 3rem;
            color: #0f1e45;
            font-weight: 800;
            margin-bottom: 1.5rem;
        }
        .hero p {
            font-size: 1.15rem;
            color: #333;
            line-height: 1.75;
        }
        .auth-box {
            padding: 2rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
            width: 100%;
            max-width: 400px;
            margin-left: auto;
        }
        .media-preview {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
            background: white;
            box-shadow: 0 0 8px rgba(0,0,0,0.03);
        }
        .screenshot-placeholder {
            width: 90%;
            max-width: 800px;
            border-radius: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="top-nav">
            <div><strong>PTW Intelligence Suite</strong></div>
            <div class="nav-links">
                <a href="#">Log in</a>
                <a href="#">Register</a>
            </div>
        </div>

        <div class="hero">
            <div class="hero-text">
                <h1>Price-to-Win Intelligence Suite</h1>
                <p>Optimize your federal contracting strategy with data-driven insights and real-time market analysis using scenario-based modeling, and AI-powered statistical analysis.</p>
            </div>
            <div class="auth-box">
    """, unsafe_allow_html=True)

    render_auth_page()

    st.markdown("""
            </div>
        </div>

        <div class="media-preview">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_placeholder.png" class="screenshot-placeholder">
        </div>
    """, unsafe_allow_html=True)

def main_app():
    initialize_session_state()

    if not st.session_state.get("is_authenticated"):
        render_landing_page()
        return

    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_placeholder.png", width=140)
        st.title("📘 Navigation")

        tabs = [
            "🏠 Home",
            "📈 Data Integration",
            "🔍 SAM Vendor Lookup",
            "💳 Manage Subscription",
            "🛠️ Admin Dashboard",
            "🔐 Logout",
        ]
        selected_tab = st.radio("Select a section:", tabs)

        st.markdown(f"""
            <div style='margin-top:2rem;'>
                <strong>Logged in as:</strong> {st.session_state.get("login_email", "User")}<br>
                <em>Role:</em> {st.session_state.get("user_role", "member")}
            </div>
        """, unsafe_allow_html=True)

    st.title("📊 Price-to-Win Intelligence Suite")

    if selected_tab.endswith("Home"):
        st.subheader("Welcome Back!")
        st.info("Use the sidebar to navigate to different tools and dashboards.")

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
        st.session_state.is_authenticated = False
        st.session_state.login_email = None
        st.session_state.user_role = None
        st.success("✅ Logged out successfully. Please refresh.")

if __name__ == "__main__":
    main_app()

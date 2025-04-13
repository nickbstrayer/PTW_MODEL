import streamlit as st
from Scripts.streamlit_auth import render_auth_page, initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab

# New: import the auth landing logic
import auth_landing_page

st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    layout="wide",
    page_icon="📊"
)

# Initialize session state
initialize_session_state()

# Handle session-based navigation
if "page" not in st.session_state:
    st.session_state.page = "landing"

def navigate(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()

# UI Layout: Based on state
if st.session_state.page == "landing":
    # Header Bar
    st.markdown("""
        <style>
        .top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2rem;
            background-color: #0f1e45;
            color: white;
        }
        .nav-links a {
            margin-left: 1.5rem;
            font-weight: 500;
            color: white;
            text-decoration: none;
        }
        .hero-section {
            display: flex;
            justify-content: space-between;
            padding: 3rem 2rem;
            background-color: #f8f9fb;
        }
        .hero-left {
            max-width: 50%;
        }
        .hero-title {
            font-size: 3rem;
            color: #0f1e45;
            font-weight: 800;
        }
        .hero-subtitle {
            font-size: 1.25rem;
            color: #333;
            margin-top: 1rem;
            margin-bottom: 2rem;
        }
        .cta-button {
            padding: 0.75rem 2rem;
            background-color: #0f1e45;
            color: white;
            font-weight: 600;
            border: none;
            border-radius: 6px;
            font-size: 1rem;
            cursor: pointer;
        }
        .hero-image {
            width: 40%;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # HTML header and button routing
    st.markdown(f"""
        <div class="top-header">
            <div><strong>PTW Intelligence Suite</strong></div>
            <div class="nav-links">
                <a href="#" onclick="window.location.href='?page=auth'">Login</a>
                <a href="#" onclick="window.location.href='?page=auth'">Register</a>
            </div>
        </div>
        <div class="hero-section">
            <div class="hero-left">
                <div class="hero-title">Price-to-Win Intelligence Suite</div>
                <div class="hero-subtitle">
                    Optimize your federal contracting strategy with data-driven insights and real-time market analysis using scenario-based modeling and AI-powered statistical analysis.
                </div>
                <button class="cta-button" onclick="window.location.href='?page=auth'">Get Started</button>
            </div>
            <img class="hero-image" src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_placeholder.png" alt="Dashboard Screenshot" />
        </div>
    """, unsafe_allow_html=True)

    # JavaScript handles href routing; catch query param here
    if st.query_params.get("page") == "auth":
        navigate("auth")

elif st.session_state.page == "auth":
    auth_landing_page.render_auth_landing_page()

elif st.session_state.page == "main":
    with st.sidebar:
        st.title("📘 Navigation")
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_placeholder.png", width=160)
        selection = st.radio("Menu", [
            "🏠 Home", 
            "📈 Data Integration", 
            "🔍 SAM Vendor Lookup",
            "💳 Manage Subscription", 
            "🛠️ Admin Dashboard", 
            "🔐 Logout"
        ])
        st.markdown(f"Logged in as: `{st.session_state.get('login_email', 'guest')}`")

    st.title("📊 Price-to-Win Intelligence Suite")

    if selection == "🏠 Home":
        st.success("Welcome to your dashboard.")
    elif selection == "📈 Data Integration":
        render_data_integration_tab()
    elif selection == "🔍 SAM Vendor Lookup":
        render_sam_vendor_lookup_tab()
    elif selection == "💳 Manage Subscription":
        render_stripe_billing_tab()
    elif selection == "🛠️ Admin Dashboard":
        if st.session_state.get("user_role") == "admin":
            render_admin_dashboard_tab()
        else:
            st.warning("🔒 Admin access only.")
    elif selection == "🔐 Logout":
        for key in ["is_authenticated", "login_email", "user_role", "page"]:
            st.session_state.pop(key, None)
        st.success("🔓 Logged out. Refreshing...")
        st.rerun()

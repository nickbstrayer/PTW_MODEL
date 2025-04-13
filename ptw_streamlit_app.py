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
    if "show_register" not in st.session_state:
        st.session_state.show_register = True
    if "login_email" not in st.session_state:
        st.session_state.login_email = ""
    if "login_password" not in st.session_state:
        st.session_state.login_password = ""

    st.markdown("""
        <style>
        body {
            font-family: 'Segoe UI', sans-serif;
        }
        .top-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.25rem 2rem;
            background-color: #0f1e45;
            color: white;
            font-size: 1.25rem;
            font-weight: 600;
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
            gap: 2rem;
            padding: 3rem 2rem;
            background-color: #f8f9fb;
        }
        .hero-text h1 {
            font-size: 3rem;
            font-weight: 800;
            color: #0f1e45;
            margin-bottom: 1rem;
        }
        .hero-text p {
            font-size: 1.125rem;
            color: #333;
            margin-bottom: 2rem;
            line-height: 1.6;
        }
        .cta-button {
            padding: 0.75rem 2rem;
            background-color: #0f1e45;
            color: white;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .auth-box {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
            max-width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navigation Bar
    st.markdown(f"""
        <div class="top-nav">
            <div>PTW Intelligence Suite</div>
            <div class="nav-links">
                <a href="#" onClick="window.location.reload();">Log in</a>
                <a href="#" onClick="window.location.reload();">Register</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Main hero + form layout
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            <div class="hero-text">
                <h1>Price-to-Win Intelligence Suite</h1>
                <p>Optimize your federal contracting strategy with data-driven insights and real-time market analysis using scenario-based modeling, and AI-powered statistical analysis.</p>
                <button class="cta-button" onClick="window.location.reload();">Get Started</button>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="auth-box">""", unsafe_allow_html=True)
        st.subheader("Register" if st.session_state.show_register else "Log In")
        st.session_state.login_email = st.text_input("Email address", value=st.session_state.login_email, key="email_input_landing")
        st.session_state.login_password = st.text_input("Password", type="password", value=st.session_state.login_password, key="password_input_landing")

        if st.session_state.show_register:
            if st.button("Sign up"):
                st.session_state.is_authenticated = True
                st.session_state.user_role = "member"
                st.success("✅ Registered and logged in.")
                st.experimental_rerun()
        else:
            if st.button("Log In"):
                if st.session_state.login_email == "admin" and st.session_state.login_password == "admin123":
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "admin"
                    st.success("✅ Welcome Admin!")
                    st.experimental_rerun()
                elif st.session_state.login_email and st.session_state.login_password:
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "member"
                    st.success("✅ Welcome back!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid credentials.")

        toggle_text = "Already have an account? Log in" if st.session_state.show_register else "Don't have an account? Register"
        if st.button(toggle_text):
            st.session_state.show_register = not st.session_state.show_register
            st.experimental_rerun()

        st.markdown("""</div>""", unsafe_allow_html=True)

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

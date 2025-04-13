import streamlit as st
from Scripts.streamlit_auth import initialize_session_state
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
            display: flex;
            justify-content: space-between;
            padding: 3rem 2rem;
            background-color: #f8f9fb;
        }
        .hero-text {
            flex: 1;
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
            max-width: 400px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="top-nav">
            <div>PTW Intelligence Suite</div>
            <div class="nav-links">
                <a href="#" onclick="window.location.reload()">Log in</a>
                <a href="#" onclick="window.location.reload()">Register</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            <div class="hero-text">
                <h1>Price-to-Win Intelligence Suite</h1>
                <p>Optimize your federal contracting strategy with data-driven insights and real-time market analysis using scenario-based modeling, and AI-powered statistical analysis.</p>
                <button class="cta-button" onclick="window.location.reload()">Get Started</button>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="auth-box">', unsafe_allow_html=True)
        st.subheader("Register" if st.session_state.show_register else "Log In")

        st.session_state.login_email = st.text_input("Email address", key="login_email")
        st.session_state.login_password = st.text_input("Password", type="password", key="login_password")

        if st.session_state.show_register:
            if st.button("Sign up"):
                st.session_state.is_authenticated = True
                st.session_state.user_role = "member"
                st.session_state.page = "main"
                st.success("✅ Registered and logged in.")
                st.rerun()
        else:
            if st.button("Log In"):
                if st.session_state.login_email == "admin" and st.session_state.login_password == "admin123":
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "admin"
                    st.session_state.page = "main"
                    st.success("✅ Welcome Admin!")
                    st.rerun()
                elif st.session_state.login_email and st.session_state.login_password:
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "member"
                    st.session_state.page = "main"
                    st.success("✅ Welcome back!")
                    st.rerun()
                else:
                    st.error("Invalid credentials.")

        toggle_text = "Already have an account? Log in" if st.session_state.show_register else "Don't have an account? Register"
        if st.button(toggle_text):
            st.session_state.show_register = not st.session_state.show_register
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

def main_app():
    initialize_session_state()

    if "is_authenticated" not in st.session_state:
        st.session_state.is_authenticated = False
    if "page" not in st.session_state:
        st.session_state.page = "landing"
    if "show_register" not in st.session_state:
        st.session_state.show_register = True
    if "login_email" not in st.session_state:
        st.session_state.login_email = ""
    if "login_password" not in st.session_state:
        st.session_state.login_password = ""

    if not st.session_state.is_authenticated or st.session_state.page != "main":
        render_landing_page()
        return

    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_placeholder.png", width=120)
        st.title("Navigation")
        tabs = [
            "🏠 Home",
            "📈 Data Integration",
            "🔍 SAM Vendor Lookup",
            "💳 Manage Subscription",
            "🛠️ Admin Dashboard",
            "🔐 Logout"
        ]
        selected = st.radio("Select page", tabs)

        st.markdown(f"""
            <div style='margin-top:2rem;'>
                <strong>Logged in as:</strong> {st.session_state.login_email}<br>
                <em>Role:</em> {st.session_state.user_role}
            </div>
        """, unsafe_allow_html=True)

    st.title("📊 Price-to-Win Intelligence Suite")

    if selected.endswith("Home"):
        st.subheader("Welcome to your PTW dashboard.")
    elif selected.endswith("Data Integration"):
        render_data_integration_tab()
    elif selected.endswith("SAM Vendor Lookup"):
        render_sam_vendor_lookup_tab()
    elif selected.endswith("Manage Subscription"):
        render_stripe_billing_tab()
    elif selected.endswith("Admin Dashboard"):
        if st.session_state.user_role == "admin":
            render_admin_dashboard_tab()
        else:
            st.warning("⚠️ You do not have admin privileges.")
    elif selected.endswith("Logout"):
        st.session_state.is_authenticated = False
        st.session_state.page = "landing"
        st.experimental_rerun()

if __name__ == "__main__":
    main_app()

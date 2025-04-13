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
    initialize_session_state()

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
            cursor: pointer;
        }
        .cta-button {
            padding: 0.75rem 2rem;
            background-color: black;
            color: white;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .card {
            background-color: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        </style>
    """, unsafe_allow_html=True)

    # Navigation bar
    st.markdown("""
        <div class="top-nav">
            <div>PTW Intelligence Suite</div>
            <div class="nav-links">
                <a onclick="window.location.href='/'" style="cursor:pointer" >Home</a>
                <a onclick="window.location.href='?auth'" >Log in</a>
                <a onclick="window.location.href='?auth'" >Register</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    left_col, right_col = st.columns([1.3, 1])

    with left_col:
        st.markdown("## Price-to-Win Intelligence Suite")
        st.write("""
            Turn data into decisions.  
            Price smarter. Win faster.  
            Welcome to PTW Intelligence Suite.
        """)
        if st.button("Get Started", key="get_started"):
            st.session_state.page = "auth"
            st.rerun()

    with right_col:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Register" if st.session_state.get("show_register", True) else "Log In")

        login_email = st.text_input("Email address", key="email_input_landing")
        login_password = st.text_input("Password", type="password", key="password_input_landing")

        if st.session_state.get("show_register", True):
            if st.button("Sign up"):
                st.session_state.is_authenticated = True
                st.session_state.user_role = "member"
                st.session_state.login_email = login_email
                st.success("✅ Registered and logged in.")
                st.session_state.page = "main"
                st.rerun()
        else:
            if st.button("Log In"):
                if login_email == "admin" and login_password == "admin123":
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "admin"
                    st.session_state.login_email = login_email
                    st.success("✅ Welcome Admin!")
                    st.session_state.page = "main"
                    st.rerun()
                elif login_email and login_password:
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "member"
                    st.session_state.login_email = login_email
                    st.success("✅ Welcome back!")
                    st.session_state.page = "main"
                    st.rerun()
                else:
                    st.error("Invalid credentials.")

        toggle_text = "Already have an account? Log in" if st.session_state.get("show_register", True) else "Don't have an account? Register"
        if st.button(toggle_text):
            st.session_state.show_register = not st.session_state.get("show_register", True)
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

def render_auth_page():
    initialize_session_state()

    st.title("Authorization")
    st.markdown("""<a href="?page=landing" style="color:#0f1e45;font-weight:600">← Back to Home</a>""", unsafe_allow_html=True)

    st.markdown("""
        <style>
        .card {
            background-color: #f4f6f8;
            padding: 2rem;
            border-radius: 12px;
            margin-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Register" if st.session_state.get("show_register", True) else "Log In")

    login_email = st.text_input("Email address", key="auth_email")
    login_password = st.text_input("Password", type="password", key="auth_password")

    if st.session_state.get("show_register", True):
        if st.button("Sign up"):
            st.session_state.is_authenticated = True
            st.session_state.user_role = "member"
            st.session_state.login_email = login_email
            st.success("✅ Registered and logged in.")
            st.session_state.page = "main"
            st.rerun()
    else:
        if st.button("Log In"):
            if login_email == "admin" and login_password == "admin123":
                st.session_state.is_authenticated = True
                st.session_state.user_role = "admin"
                st.session_state.login_email = login_email
                st.success("✅ Welcome Admin!")
                st.session_state.page = "main"
                st.rerun()
            elif login_email and login_password:
                st.session_state.is_authenticated = True
                st.session_state.user_role = "member"
                st.session_state.login_email = login_email
                st.success("✅ Welcome back!")
                st.session_state.page = "main"
                st.rerun()
            else:
                st.error("Invalid credentials.")

    toggle_text = "Already have an account? Log in" if st.session_state.get("show_register", True) else "Don't have an account? Register"
    if st.button(toggle_text, key="toggle_auth"):
        st.session_state.show_register = not st.session_state.get("show_register", True)
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def render_main_app():
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
        st.session_state.page = "landing"
        st.success("✅ Logged out successfully. Please refresh.")

def main():
    initialize_session_state()

    if "page" not in st.session_state:
        st.session_state.page = "landing"

    if st.session_state.page == "auth":
        render_auth_page()
    elif st.session_state.page == "main":
        render_main_app()
    else:
        render_landing_page()

if __name__ == "__main__":
    main()

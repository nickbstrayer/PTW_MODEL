import streamlit as st

# Mocked user database (replace with secure storage later)
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "nick": {"password": "maasai123", "role": "user"},
}

def initialize_session_state():
    defaults = {
        "is_authenticated": False,
        "current_user": None,
        "user_role": None,
        "login_email": "",
        "login_password": "",
        "auth_action": "Login",  # or Register
        "logout_requested": False
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def login():
    st.session_state.login_email = st.text_input("Email", value=st.session_state.login_email)
    st.session_state.login_password = st.text_input("Password", value=st.session_state.login_password, type="password")

    if st.button("Login"):
        email = st.session_state.login_email.strip()
        password = st.session_state.login_password.strip()

        user = USERS.get(email)
        if user and user["password"] == password:
            st.session_state.is_authenticated = True
            st.session_state.current_user = email
            st.session_state.user_role = user["role"]
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid email or password.")

def logout():
    st.warning(f"🔒 Logged in as **{st.session_state.get('current_user')}**")

    with st.expander("⚠️ Confirm Logout", expanded=True):
        if st.button("Confirm Logout"):
            st.session_state.is_authenticated = False
            st.session_state.current_user = None
            st.session_state.user_role = None
            st.session_state.login_email = ""
            st.session_state.login_password = ""
            st.success("You have been logged out.")
            st.rerun()

def render_auth_page():
    initialize_session_state()

    st.markdown("## 🔐 PTW Intelligence Suite")
    st.radio("Choose Option", ["Login", "Register"], key="auth_action", horizontal=True)

    if st.session_state.auth_action == "Login":
        if st.session_state.is_authenticated:
            logout()
        else:
            login()
    else:
        st.info("Registration is currently disabled. Please contact the admin.")

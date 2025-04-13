import streamlit as st

# Hardcoded users for now
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "nick": {"password": "maasai123", "role": "user"},
}

def render_auth_page():
    st.markdown("## 🔐 PTW Intelligence Suite")
    auth_mode = st.radio("Choose Option", ["Login", "Register"], horizontal=True)

    if auth_mode == "Login":
        login()
    elif auth_mode == "Register":
        register()


def login():
    st.subheader("Sign In to Your Account")
    username = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        user = USERS.get(username)
        if user and user["password"] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.role = user["role"]
            st.experimental_rerun()
        else:
            st.error("Invalid email or password.")


def register():
    st.subheader("Create a New Account (Disabled for now)")
    st.info("Registration will be enabled in a future update.")

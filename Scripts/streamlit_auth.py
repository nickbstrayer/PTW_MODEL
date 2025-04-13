import streamlit as st

# Hardcoded credentials for now (will move to secure storage later)
VALID_USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "nick": {"password": "maasai123", "role": "user"}
}

def authenticate_user(username, password):
    user = VALID_USERS.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

def render_auth_page():
    st.markdown("## 🔐 PTW Intelligence Suite")
    st.markdown("### Sign In to Your Account")

    auth_mode = st.radio("Choose Option", ["Login", "Register"])

    if auth_mode == "Login":
        username = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            role = authenticate_user(username, password)
            if role:
                st.session_state["logged_in"] = True
                st.session_state["user_role"] = role
                st.session_state["username"] = username
                st.rerun()
            else:
                st.error("Invalid email or password.")

    elif auth_mode == "Register":
        st.info("🚧 Registration coming soon. Contact admin to request access.")

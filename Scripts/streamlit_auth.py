import streamlit as st

# Hardcoded user credentials for now
VALID_USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "nick": {"password": "maasai123", "role": "user"}
}

def authenticate_user(username, password):
    user = VALID_USERS.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

def login_form():
    st.markdown("## 🔐 PTW Intelligence Suite")
    auth_mode = st.radio("Choose Option", ["Login", "Register"])

    if auth_mode == "Login":
        username = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")

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
        st.info("🚧 Registration is currently disabled in this demo.")

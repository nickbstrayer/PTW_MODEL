import streamlit as st
import hashlib

# Simulated user database
USER_CREDENTIALS = {
    "admin": "admin123",
    "nick": "maasai123",
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_credentials(username, password):
    if username in USER_CREDENTIALS:
        return USER_CREDENTIALS[username] == password
    return False

def login():
    st.subheader("Sign In to Your Account")
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        if check_credentials(email, password):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.rerun()  # Updated method here
        else:
            st.error("Invalid email or password.")

def register():
    st.subheader("Register New Account")
    new_email = st.text_input("Email", key="register_email")
    new_password = st.text_input("Password", type="password", key="register_password")
    if st.button("Register"):
        if new_email and new_password:
            if new_email not in USER_CREDENTIALS:
                USER_CREDENTIALS[new_email] = new_password
                st.success("Registration successful. Please log in.")
            else:
                st.error("User already exists.")
        else:
            st.warning("Please enter both email and password.")

def render_auth_page():
    st.markdown("### 🔐 PTW Intelligence Suite")
    auth_mode = st.radio("Choose Option", ["Login", "Register"], horizontal=True)
    if auth_mode == "Login":
        login()
    else:
        register()

import streamlit as st
import hashlib
import json
from pathlib import Path

# Path to mock user database (stored in the same directory)
USER_DB = Path("users.json")

# Load existing user accounts
def load_users():
    if USER_DB.exists():
        with open(USER_DB, "r") as f:
            return json.load(f)
    return {}

# Save user accounts
def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=2)

# Secure hash function for passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Main Login/Register UI tab
def render_auth_page():
    st.title("🔐 PTW Intelligence Suite")

    tab = st.radio("Choose Option", ["Login", "Register"])
    users = load_users()

    if tab == "Register":
        st.subheader("Create a New Account")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_pass")
        confirm = st.text_input("Confirm Password", type="password", key="reg_pass2")

        if st.button("Register"):
            if not email or not password or not confirm:
                st.warning("Please fill in all fields.")
            elif password != confirm:
                st.error("Passwords do not match.")
            elif email in users:
                st.error("An account with this email already exists.")
            else:
                users[email] = hash_password(password)
                save_users(users)
                st.success("Registration successful! Please log in.")

    elif tab == "Login":
        st.subheader("Sign In to Your Account")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            if email in users and users[email] == hash_password(password):
                st.session_state["user"] = email
                st.success(f"Welcome back, {email}!")
            else:
                st.error("Invalid email or password.")

    # Optional display of current user
    if "user" in st.session_state:
        st.info(f"🔓 Logged in as: {st.session_state['user']}")

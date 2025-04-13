import streamlit as st

# Simulated user database
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "demo": {"password": "demo123", "role": "user"},
}

def login():
    st.subheader("\U0001F511 PTW Intelligence Suite")

    auth_mode = st.radio("Choose Option", ["Login", "Register"], horizontal=True)

    if auth_mode == "Register":
        new_email = st.text_input("Create Username")
        new_password = st.text_input("Create Password", type="password")
        role = st.selectbox("Role", ["user", "admin"])
        if st.button("Register"):
            if new_email and new_password:
                if new_email in USERS:
                    st.error("Username already exists.")
                else:
                    USERS[new_email] = {"password": new_password, "role": role}
                    st.success("Registered successfully. Please login.")
                    st.experimental_rerun()
            else:
                st.warning("Please fill in both fields.")
    else:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if email in USERS and USERS[email]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.username = email
                st.session_state.role = USERS[email]["role"]
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error("Invalid email or password.")

def logout():
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.sidebar.success("Logged out successfully.")
        st.experimental_rerun()

def render_auth_page():
    login()

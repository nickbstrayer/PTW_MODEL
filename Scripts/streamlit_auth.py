import streamlit as st

# Dummy in-memory store for example
if "users" not in st.session_state:
    st.session_state.users = {"admin": "admin"}  # default admin login

def initialize_session_state():
    if "is_authenticated" not in st.session_state:
        st.session_state.is_authenticated = False
    if "login_email" not in st.session_state:
        st.session_state.login_email = ""
    if "user_role" not in st.session_state:
        st.session_state.user_role = ""
    if "page" not in st.session_state:
        st.session_state.page = "landing"

def render_auth_page():
    mode = st.query_params.get("mode", "register")

    st.markdown(
        '<h3 style="margin-top:0; margin-bottom: 1rem;"><span style="font-size:1.8rem;">🔐 PTW Intelligence Suite</span></h3>',
        unsafe_allow_html=True
    )

    auth_mode = st.radio("Choose Option", ["Login", "Register"], index=0 if mode == "login" else 1)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if auth_mode == "Login":
        if st.button("Login"):
            if email in st.session_state.users and st.session_state.users[email] == password:
                st.session_state.is_authenticated = True
                st.session_state.login_email = email
                st.session_state.user_role = "admin" if email == "admin" else "member"
                st.session_state.page = "main"
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials.")
    else:
        if st.button("Register"):
            if email and password:
                st.session_state.users[email] = password
                st.session_state.is_authenticated = True
                st.session_state.login_email = email
                st.session_state.user_role = "member"
                st.session_state.page = "main"
                st.success("🎉 Registration complete. You're now logged in.")
                st.rerun()
            else:
                st.warning("⚠️ Please provide both email and password.")

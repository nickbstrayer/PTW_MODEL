import streamlit as st

# Simulated user database (replace with secure authentication in production)
USER_DB = {
    "admin": "admin",  # username: password
    "user@example.com": "password123"
}

def initialize_session_state():
    if "is_authenticated" not in st.session_state:
        st.session_state.is_authenticated = False
    if "login_email" not in st.session_state:
        st.session_state.login_email = ""
    if "user_role" not in st.session_state:
        st.session_state.user_role = "member"
    if "page" not in st.session_state:
        st.session_state.page = "landing"

def render_auth_page():
    mode = st.query_params.get("mode", ["login"])[0]

    st.markdown("### 🔐 PTW Intelligence Suite")
    st.radio("Choose Option", ["Login", "Register"], index=0 if mode == "login" else 1, key="auth_mode", horizontal=True)

    email = st.text_input("Email", key="email_input")
    password = st.text_input("Password", type="password", key="password_input")

    if st.session_state.auth_mode == "Login":
        if st.button("Login"):
            if email in USER_DB and USER_DB[email] == password:
                st.session_state.is_authenticated = True
                st.session_state.login_email = email
                st.session_state.user_role = "admin" if email == "admin" else "member"
                st.session_state.page = "main"
                st.rerun()
            else:
                st.error("❌ Invalid credentials.")
    else:
        if st.button("Register"):
            if email and password:
                if email not in USER_DB:
                    USER_DB[email] = password
                    st.success("🎉 Registration complete. You're now logged in.")
                    st.session_state.is_authenticated = True
                    st.session_state.login_email = email
                    st.session_state.user_role = "member"
                    st.session_state.page = "main"
                    st.rerun()
                else:
                    st.warning("⚠️ User already exists.")
            else:
                st.warning("⚠️ Please enter email and password.")

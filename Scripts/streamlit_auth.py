import streamlit as st

# Sample hardcoded users (you can replace with database or secure auth system later)
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"},
}

def login():
    st.session_state.login_email = st.text_input("Email", key="login_email")
    st.session_state.login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        email = st.session_state.login_email
        password = st.session_state.login_password

        if email in USERS and USERS[email]["password"] == password:
            st.success("Login successful!")
            st.session_state.is_authenticated = True
            st.session_state.user_role = USERS[email]["role"]
            st.session_state.current_user = email
            st.rerun()  # ✅ Updated from experimental_rerun()
        else:
            st.error("Invalid email or password.")

def register():
    st.warning("Registration is not yet implemented.")

def logout():
    if st.session_state.get("is_authenticated"):
        with st.expander("⚠️ Confirm Logout", expanded=True):
            if st.button("Confirm Logout"):
                st.session_state.is_authenticated = False
                st.session_state.user_role = None
                st.session_state.current_user = None
                st.success("You have been logged out.")
                st.rerun()  # ✅ Updated from experimental_rerun()

def render_auth_page():
    st.markdown("## 🔐 PTW Intelligence Suite")

    if "auth_option" not in st.session_state:
        st.session_state.auth_option = "Login"

    auth_choice = st.radio("Choose Option", ["Login", "Register"], index=0, key="auth_choice")

    if auth_choice == "Login":
        login()
    else:
        register()

    # Optional logout option shown if user is logged in
    if st.session_state.get("is_authenticated"):
        st.divider()
        st.write(f"🔓 Logged in as **{st.session_state.current_user}**")
        logout()

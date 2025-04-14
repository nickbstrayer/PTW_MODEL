import streamlit as st

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
    query_params = st.query_params if hasattr(st, 'query_params') else st.experimental_get_query_params()
    mode = query_params.get("mode", ["login"])[0]

    st.markdown("### 🔐 PTW Intelligence Suite")

    if st.session_state.get("is_authenticated"):
        st.success(f"🔓 Logged in as **{st.session_state['login_email']}**")
        with st.expander("⚠️ Confirm Logout"):
            if st.button("Confirm Logout"):
                st.session_state.is_authenticated = False
                st.session_state.login_email = ""
                st.session_state.page = "landing"
                st.experimental_rerun()
        return

    st.radio("Choose Option", ["Login", "Register"], index=0 if mode == "login" else 1, key="auth_mode", horizontal=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.session_state.auth_mode == "Login":
        if st.button("Login"):
            if email and password:
                # Example hardcoded check - replace with actual auth logic
                st.session_state.is_authenticated = True
                st.session_state.login_email = email
                st.session_state.user_role = "admin" if email == "admin@example.com" else "member"
                st.session_state.page = "main"
                st.experimental_rerun()
            else:
                st.error("Please enter both email and password.")
    else:
        if st.button("Register"):
            if email and password:
                st.session_state.is_authenticated = True
                st.session_state.login_email = email
                st.session_state.user_role = "member"
                st.session_state.page = "main"
                st.success("🎉 Registration complete. You're now logged in.")
                st.experimental_rerun()
            else:
                st.error("Please complete all fields to register.")

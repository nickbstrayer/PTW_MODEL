import streamlit as st
from Scripts.streamlit_auth import initialize_session_state

st.set_page_config(
    page_title="Login | Register - PTW Intelligence Suite",
    layout="centered",
    page_icon="🔐"
)

def render_auth_form():
    initialize_session_state()

    st.markdown("""
        <style>
        .auth-box {
            background: white;
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 0 12px rgba(0,0,0,0.08);
            max-width: 480px;
            margin: 3rem auto;
        }
        .auth-box h2 {
            text-align: center;
            font-size: 1.75rem;
            margin-bottom: 1.5rem;
            color: #0f1e45;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
        mode = "Register" if st.session_state.get("show_register", True) else "Log In"
        st.markdown(f"<h2>{mode}</h2>", unsafe_allow_html=True)

        email = st.text_input("Email address", key="auth_email")
        password = st.text_input("Password", type="password", key="auth_password")

        if st.session_state.get("show_register", True):
            if st.button("Sign up"):
                st.session_state.is_authenticated = True
                st.session_state.user_role = "member"
                st.session_state.login_email = email
                st.success("✅ Registered and logged in.")
                st.switch_page("ptw_streamlit_app.py")
        else:
            if st.button("Log in"):
                if email == "admin" and password == "admin123":
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "admin"
                    st.session_state.login_email = email
                    st.success("✅ Welcome Admin!")
                    st.switch_page("ptw_streamlit_app.py")
                elif email and password:
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "member"
                    st.session_state.login_email = email
                    st.success("✅ Welcome back!")
                    st.switch_page("ptw_streamlit_app.py")
                else:
                    st.error("Invalid credentials.")

        toggle_label = "Already have an account? Log in" if st.session_state.get("show_register", True) else "Don't have an account? Register"
        if st.button(toggle_label):
            st.session_state.show_register = not st.session_state.get("show_register", True)
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    render_auth_form()

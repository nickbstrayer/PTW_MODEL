import streamlit as st

# In-memory user store for demo
users = {
    "admin": {"password": "admin", "role": "admin"},
    "user": {"password": "user", "role": "member"}
}

def initialize_session_state():
    if "is_authenticated" not in st.session_state:
        st.session_state.is_authenticated = False
    if "login_email" not in st.session_state:
        st.session_state.login_email = None
    if "user_role" not in st.session_state:
        st.session_state.user_role = None
    if "page" not in st.session_state:
        st.session_state.page = "landing"

def render_auth_page():
    mode = st.query_params.get("mode", ["login"])[0]

    st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <h2 style="font-size: 1.75rem; margin-bottom: 1rem;">🔐 PTW Intelligence Suite</h2>
        </div>
    """, unsafe_allow_html=True)

    st

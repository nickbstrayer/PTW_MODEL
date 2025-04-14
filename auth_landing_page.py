import streamlit as st
from Scripts.streamlit_auth import render_auth_page as streamlit_render_auth_page, initialize_session_state

# This page is only for authorization (Login/Register)
def render_auth_page():
    st.set_page_config(
        page_title="Authorization | PTW Intelligence Suite",
        layout="wide",
        page_icon="🔐"
    )

    initialize_session_state()

    # Safely get mode (login or register)
    try:
        query_params = st.query_params if hasattr(st, 'query_params') else st.experimental_get_query_params()
    except:
        query_params = st.experimental_get_query_params()

    mode = query_params.get("mode", ["register"])[0]
    st.markdown("""
        <style>
            .top-nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem 2rem;
                background-color: #0f1e45;
                color: white;
                font-size: 1.25rem;
                font-weight: 600;
            }
            .nav-links a {
                margin-left: 1.5rem;
                color: white;
                text-decoration: none;
                font-weight: 500;
            }
            .auth-card {
                background-color: white;
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
            }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
        <div class="top-nav">
            <div>PTW Intelligence Suite</div>
            <div class="nav-links">
                <a href="?page=auth&mode=login">Log in</a>
                <a href="?page=auth&mode=register">Register</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("[← Back to Home](?page=landing)", unsafe_allow_html=True)

    # Title
    st.title("Authorization")
    st.subheader("Please {} to continue".format("log in" if mode == "login" else "register"))
    st.info("Enter your credentials below.")

    # Main Layout
    left_col, right_col = st.columns([1, 1])
    with left_col:
        st.markdown("""
            ### About PTW Suite
            Use our platform to model, analyze, and enhance your contract pricing strategy.
            Gain real-time insights, benchmark data, and competitive intelligence.
        """)

    with right_col:
        with st.container():
            st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
            streamlit_render_auth_page()
            st.markdown("</div>", unsafe_allow_html=True)

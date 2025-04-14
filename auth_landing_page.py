import streamlit as st
from Scripts.streamlit_auth import render_auth_page as streamlit_render_auth_page, initialize_session_state

# This page is only for authorization (Login/Register)
# The set_page_config must be moved out of this function and to the TOP-LEVEL ptw_streamlit_app.py

def render_auth_page():
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
                padding: 1.25rem 2rem;
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
            .auth-layout {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 3rem;
                margin-top: 2rem;
                padding: 0 2rem;
            }
            .auth-left h3 {
                margin-bottom: 1rem;
            }
            .auth-left ul {
                list-style: disc;
                padding-left: 1.5rem;
                color: #333;
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

    # Breadcrumb trail
    st.markdown("[← Back to Home](?page=landing)", unsafe_allow_html=True)

    # Title and Intro
    st.markdown("""
        <div style='padding: 1rem 2rem;'>
            <h1>Authorization</h1>
            <h3>Please {}</h3>
            <div style='margin-top: 1rem;'>
                <div style='background-color: #e6f1fc; padding: 1rem; border-radius: 8px;'>
                    Use your credentials to access the PTW Intelligence Suite.
                </div>
            </div>
        </div>
    """.format("log in" if mode == "login" else "register"), unsafe_allow_html=True)

    # Layout
    st.markdown("<div class='auth-layout'>", unsafe_allow_html=True)

    st.markdown("""
        <div class='auth-left'>
            <h3>Why PTW?</h3>
            <ul>
                <li>Data-driven pricing strategy</li>
                <li>Real-time benchmarks</li>
                <li>Win-rate insights powered by AI</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='auth-right'><div class='auth-card'>", unsafe_allow_html=True)
    streamlit_render_auth_page()
    st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # End layout div

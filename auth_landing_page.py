# auth_landing_page.py

import streamlit as st
from Scripts.streamlit_auth import render_auth_page, initialize_session_state

def render_landing_page():
    initialize_session_state()

    st.set_page_config(page_title="Authorization | PTW Intelligence Suite", layout="wide", page_icon="🔐")

    st.markdown("""
        <style>
        .breadcrumb a {
            font-size: 0.95rem;
            text-decoration: none;
            color: #0f1e45;
            margin-bottom: 1rem;
            display: inline-block;
        }
        .auth-box {
            background-color: #f5f8fc;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .auth-header {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }
        .auth-subtext {
            font-size: 1rem;
            color: #555;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='breadcrumb'><a href='/?page=landing'>&larr; Back to Home</a></div>", unsafe_allow_html=True)
    
    left, right = st.columns([1.2, 1])
    
    with left:
        st.markdown("<div class='auth-header'>Welcome to the PTW Intelligence Suite</div>", unsafe_allow_html=True)
        st.markdown("<div class='auth-subtext'>Please log in or register to continue. Your credentials will allow access to all integrated dashboards and benchmarking tools.</div>", unsafe_allow_html=True)

    with right:
        with st.container():
            st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
            render_auth_page()
            st.markdown("</div>", unsafe_allow_html=True)

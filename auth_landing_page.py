import streamlit as st
from Scripts.streamlit_auth import render_auth_page as streamlit_render_auth_page, initialize_session_state

# ✅ MUST BE FIRST Streamlit command
st.set_page_config(
    page_title="Authorization | PTW Intelligence Suite",
    layout="wide",
    page_icon="🔐"
)

# ✅ This page is only for authorization (Login/Register)
def render_auth_page():
    initialize_session_state()

    # Safely get mode (login or register)
    try:
        query_params = st.query_params if hasattr(st, 'query_params') else st.experimental_get_query_params()
    except:
        query_params = st.experimental_get_query_params()

    mode = query_params.get("mode", ["register"])[0]

    # Inject style
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

    # Top nav bar
    st.markdown("""
        <div class="top-nav">
            <div>PTW Intelligence Suite</div>
            <div class="nav-links">
                <a href="?page=auth&mode=login">Log in</a>
                <a href="?page=auth&mode=register">Register</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Breadcrumb
    st.markdown("[← Back to Home](?page=landing)", unsafe_allow_html=True)

    # Page title and instructions
    st.title("Authorization")
    st.subheader("Please {} to continue".format("log in" if mode == "login" else "register"))
    st.info("Use your credentials to access the PTW Intelligence Suite.")

    # Main layout
    left_col, right_col = st.columns([1, 1])
    with left_col:
        st.markdown("""
            ### Why PTW?
            - Data-driven pricing strategy
            - Real-time benchmarks
            - Win-rate insights powered by AI
        """)

    with right_col:
        with st.container():
            st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
            streamlit_render_auth_page()
            st.markdown("</div>", unsafe_allow_html=True)

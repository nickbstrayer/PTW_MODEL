import streamlit as st
from Scripts.streamlit_auth import initialize_session_state

def render_landing_page():
    initialize_session_state()

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
        .cta-button {
            padding: 0.75rem 2rem;
            background-color: black;
            color: white;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .card {
            background-color: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        .breadcrumb {
            font-size: 0.875rem;
            margin: 1rem 2rem;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="top-nav">
            <div>PTW Intelligence Suite</div>
            <div class="nav-links">
                <a href="/?page=auth">Log in</a>
                <a href="/?page=auth">Register</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="breadcrumb">
            ← <a href="/">Back to Home</a>
        </div>
    """, unsafe_allow_html=True)

    # Hero + Register Split
    left_col, right_col = st.columns([1.3, 1])

    with left_col:
        st.markdown("## Welcome to PTW Intelligence Suite")
        st.markdown("""
            Turn data into decisions.
            Price smarter. Win faster.

            Use our platform to model, analyze, and enhance your contract pricing strategy through real-time benchmarking and AI-powered insights.
        """)

    with right_col:
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("Register" if st.session_state.get("show_register", True) else "Log In")

            login_email = st.text_input("Email address", key="email_input_landing")
            login_password = st.text_input("Password", type="password", key="password_input_landing")

            if st.session_state.get("show_register", True):
                if st.button("Sign up"):
                    st.session_state.is_authenticated = True
                    st.session_state.user_role = "member"
                    st.session_state.login_email = login_email
                    st.success("\u2705 Registered and logged in.")
                    st.session_state.page = "main"
                    st.rerun()
            else:
                if st.button("Log In"):
                    if login_email == "admin" and login_password == "admin123":
                        st.session_state.is_authenticated = True
                        st.session_state.user_role = "admin"
                        st.session_state.login_email = login_email
                        st.success("\u2705 Welcome Admin!")
                        st.session_state.page = "main"
                        st.rerun()
                    elif login_email and login_password:
                        st.session_state.is_authenticated = True
                        st.session_state.user_role = "member"
                        st.session_state.login_email = login_email
                        st.success("\u2705 Welcome back!")
                        st.session_state.page = "main"
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")

            toggle_text = "Already have an account? Log in" if st.session_state.get("show_register", True) else "Don't have an account? Register"
            if st.button(toggle_text):
                st.session_state.show_register = not st.session_state.get("show_register", True)
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

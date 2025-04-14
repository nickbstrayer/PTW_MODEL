import streamlit as st
from Scripts.streamlit_auth import render_auth_page, initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab
from auth_landing_page import render_auth_page  # Correct function for authorization

# Set page config as the first Streamlit command
st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    layout="wide",
    page_icon="📊"
)

def main_app():
    initialize_session_state()

    # Use the new query_params method
    query_params = st.query_params
    page = query_params.get("page", ["landing"])[0]

    if not st.session_state.get("is_authenticated") or st.session_state.get("page") != "main":
        render_auth_page()
        return

    # Header navigation
    st.markdown("""
        <div style="background-color:#0f1e45; padding:1rem; display:flex; justify-content:space-between; align-items:center;">
            <div style="color:white; font-size:1.5rem; font-weight:600;">PTW Intelligence Suite</div>
            <div>
                <a href="?page=auth&mode=login" style="color:white; margin-right:1.5rem; text-decoration:none; font-weight:500;">Log in</a>
                <a href="?page=auth&mode=register" style="color:white; text-decoration:none; font-weight:500;">Register</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Hero and Auth CTA Split Layout with proper alignment and spacing
    st.markdown("""
        <style>
            .container {
                display: flex;
                justify-content: space-between;
                padding: 2rem 1rem;
            }
            .hero-box, .auth-box {
                background: white;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                width: 48%;
            }
            .hero-box h2 {
                font-size: 2rem;
                margin-bottom: 0.5rem;
            }
            .hero-box p {
                font-size: 1.125rem;
                margin: 0.25rem 0;
            }
        </style>
        <div class="container">
            <div class="hero-box">
                <h2>Price-to-Win Intelligence Suite</h2>
                <p>Turn data into decisions.</p>
                <p>Price smarter. Win faster.</p>
                <p>Welcome to PTW Intelligence Suite.</p>
                <a href="?page=auth&mode=register">
                    <button style="margin-top:1rem; padding:0.5rem 1.5rem; font-size:1rem; font-weight:500; background-color:#0f1e45; color:white; border:none; border-radius:5px; cursor:pointer;">Get Started</button>
                </a>
            </div>
            <div class="auth-box">
    """, unsafe_allow_html=True)

    render_auth_page()

    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main_app()

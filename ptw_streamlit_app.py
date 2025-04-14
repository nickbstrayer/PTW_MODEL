import streamlit as st
from Scripts.streamlit_auth import initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab
from auth_landing_page import render_auth_page  # Corrected import

# This must be the first Streamlit command
st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    layout="wide",
    page_icon="📊"
)

def main_app():
    initialize_session_state()

    try:
        query_params = st.query_params if hasattr(st, 'query_params') else st.experimental_get_query_params()
    except:
        query_params = st.experimental_get_query_params()

    page = query_params.get("page", ["landing"])[0]

    if page == "auth":
        render_auth_page()
        return

    if not st.session_state.get("is_authenticated") or st.session_state.get("page") != "main":
        render_landing_page()
        return

    # Authenticated user main app
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_placeholder.png", width=140)
        st.title("📘 Navigation")
        tabs = [
            "🏠 Home",
            "📈 Data Integration",
            "🔍 SAM Vendor Lookup",
            "💳 Manage Subscription",
            "🛠️ Admin Dashboard",
            "🔐 Logout",
        ]
        selected_tab = st.radio("Select a section:", tabs)
        st.markdown(f"""
            <div style='margin-top:2rem;'>
                <strong>Logged in as:</strong> {st.session_state.get("login_email", "User")}<br>
                <em>Role:</em> {st.session_state.get("user_role", "member")}
            </div>
        """, unsafe_allow_html=True)

    st.title("📊 Price-to-Win Intelligence Suite")

    if selected_tab.endswith("Home"):
        st.subheader("Welcome Back!")
        st.info("Use the sidebar to navigate to different tools and dashboards.")
    elif selected_tab.endswith("Data Integration"):
        render_data_integration_tab()
    elif selected_tab.endswith("SAM Vendor Lookup"):
        render_sam_vendor_lookup_tab()
    elif selected_tab.endswith("Manage Subscription"):
        render_stripe_billing_tab()
    elif selected_tab.endswith("Admin Dashboard"):
        if st.session_state.get("user_role") == "admin":
            render_admin_dashboard_tab()
        else:
            st.warning("⚠️ Admin access required.")
    elif selected_tab.endswith("Logout"):
        st.session_state.is_authenticated = False
        st.session_state.login_email = None
        st.session_state.user_role = None
        st.session_state.page = "landing"
        st.success("✅ Logged out successfully. Please refresh.")


def render_landing_page():
    st.markdown("""
        <style>
            .hero-section {
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                padding: 3rem 2rem;
            }
            .hero-left {
                max-width: 50%;
            }
            .hero-left h1 {
                font-size: 2.5rem;
                font-weight: 700;
                margin-bottom: 1rem;
            }
            .hero-left p {
                font-size: 1.1rem;
                margin-bottom: 0.5rem;
            }
            .auth-card {
                padding: 2rem;
                background-color: white;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.1);
                max-width: 400px;
            }
            .top-nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #0f1e45;
                padding: 1.25rem 2rem;
                color: white;
                font-weight: 600;
            }
            .top-nav a {
                margin-left: 2rem;
                color: white;
                text-decoration: none;
            }
        </style>
    """, unsafe_allow_html=True)

    # Top Nav
    st.markdown("""
        <div class="top-nav">
            <div>PTW Intelligence Suite</div>
            <div>
                <a href="?page=auth&mode=login">Log in</a>
                <a href="?page=auth&mode=register">Register</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='hero-section'>", unsafe_allow_html=True)

    # Left Hero
    st.markdown("""
        <div class='hero-left'>
            <h1>Price-to-Win Intelligence Suite</h1>
            <p>Turn data into decisions.</p>
            <p>Price smarter. Win faster.</p>
            <p>Welcome to PTW Intelligence Suite.</p>
            <a href="?page=auth&mode=register">
                <button style='padding: 0.75rem 1.5rem; margin-top: 1rem;'>Get Started</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    # Right Auth Card
    st.markdown("""
        <div class='auth-card'>
            <h3>Register</h3>
    """, unsafe_allow_html=True)

    from Scripts.streamlit_auth import render_auth_page as render_auth_component
    render_auth_component()

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)  # Close hero-section


if __name__ == "__main__":
    main_app()

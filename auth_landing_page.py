import streamlit as st
from Scripts.streamlit_auth import render_auth_page as streamlit_render_auth_page, initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab
from auth_landing_page import render_landing_page  # Dedicated landing/auth page

st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    layout="wide",
    page_icon="📊"
)

def render_auth_page():
    st.markdown("""
        <style>
        .auth-header {
            font-size: 2.5rem;
            font-weight: 800;
            color: #0f1e45;
            margin-bottom: 0.5rem;
        }
        .auth-instructions {
            font-size: 1.1rem;
            color: #444;
            margin-bottom: 2rem;
        }
        .auth-container {
            background-color: #f5f8fc;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .breadcrumb {
            margin-bottom: 1rem;
            font-size: 0.95rem;
        }
        .breadcrumb a {
            text-decoration: none;
            color: #0f1e45;
            font-weight: 500;
        }
        .auth-section-title {
            font-size: 1.75rem;
            color: #0f1e45;
            margin-bottom: 0.5rem;
        }
        .auth-note {
            font-size: 0.95rem;
            color: #555;
            margin-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='breadcrumb'><a href='/?page=landing'>&larr; Back to Home</a></div>", unsafe_allow_html=True)
    st.markdown("<div class='auth-header'>Account Access</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='auth-instructions'>
        Please register or log in to access the PTW Intelligence Suite tools and analytics. If you don't have an account, select 'Register' to get started.
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("<div class='auth-section-title'>Create Your Account</div>", unsafe_allow_html=True)
        st.markdown("""
            Register to unlock the full capabilities of the Price-to-Win Intelligence Suite.  
            Your account gives you access to advanced tools for federal contract pricing, AI-powered insights, and real-time benchmarking.

            - Use a government or company-issued email when possible.  
            - Passwords must be at least 8 characters and include one number or symbol.
        """)

    with col2:
        st.markdown("<div class='auth-section-title'>Log In to Your Account</div>", unsafe_allow_html=True)
        st.markdown("""
            Welcome back to the Price-to-Win Intelligence Suite.  
            Enter your credentials to continue analyzing, pricing, and winning smarter.  
            If you haven’t created an account yet, click on **Register** to sign up.
        """)
        st.markdown("""
            <div class='auth-note'>🔒 Your session is secure.  
            Need help accessing your account? <a href='mailto:support@ptwsuite.com'>Contact support</a></div>
        """, unsafe_allow_html=True)

    with st.container():
        streamlit_render_auth_page()

def main_app():
    initialize_session_state()

    # Safely get the current page from query params
    try:
        query_params = st.query_params if hasattr(st, 'query_params') else st.experimental_get_query_params()
    except:
        query_params = st.experimental_get_query_params()

    page = query_params.get("page", ["landing"])[0]

    # Route to authentication page if specified
    if page == "auth":
        render_auth_page()
        return

    # Redirect unauthenticated users to landing page
    if not st.session_state.get("is_authenticated") or st.session_state.get("page") != "main":
        render_landing_page()
        return

    # Main sidebar navigation
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

    # Main content area based on selected tab
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

if __name__ == "__main__":
    main_app()

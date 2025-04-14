import streamlit as st
from Scripts.streamlit_auth import render_auth_page, initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab

# Set page config as the first Streamlit command
st.set_page_config(
    page_title="Price-to-Win Intelligence Suite",
    layout="wide",
    page_icon="📊"
)

def main_app():
    initialize_session_state()

    query_params = st.query_params
    page = query_params.get("page", ["landing"])[0]

    # If not authenticated or not on main page, show login/register interface
    if not st.session_state.get("is_authenticated") or st.session_state.get("page") != "main":
        # Header navigation for unauthenticated state
        st.markdown("""
            <div style="background-color:#0f1e45; padding:1rem; display:flex; justify-content:space-between; align-items:center;">
                <div style="color:white; font-size:1.5rem; font-weight:600;">PTW Intelligence Suite</div>
                <div>
                    <a href="?page=auth&mode=login" style="color:white; margin-right:1.5rem; text-decoration:none; font-weight:500;">Log in</a>
                    <a href="?page=auth&mode=register" style="color:white; text-decoration:none; font-weight:500;">Register</a>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Styled 2-column layout using columns
        left, right = st.columns([1, 1])
        with left:
            st.markdown("""
                <div style="background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); height: 100%;">
                    <h2 style="font-size: 2rem; margin-bottom: 0.5rem;">Price-to-Win Intelligence Suite</h2>
                    <p style="font-size: 1.125rem; margin: 0.25rem 0;">Turn data into decisions.</p>
                    <p style="font-size: 1.125rem; margin: 0.25rem 0;">Price smarter. Win faster.</p>
                    <p style="font-size: 1.125rem; margin: 0.25rem 0;">Welcome to PTW Intelligence Suite.</p>
                    <a href="?page=auth&mode=register">
                        <button style="margin-top:1rem; padding:0.5rem 1.5rem; font-size:1rem; font-weight:500; background-color:#0f1e45; color:white; border:none; border-radius:5px; cursor:pointer;">Learn More</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

        with right:
            with st.container():
                render_auth_page()
        return

    # Main app interface (authenticated)
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

if __name__ == "__main__":
    main_app()

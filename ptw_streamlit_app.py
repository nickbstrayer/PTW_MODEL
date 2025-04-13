import streamlit as st
from Scripts.streamlit_auth import render_auth_page as streamlit_render_auth_page, initialize_session_state
from Scripts.streamlit_vendor_lookup import render_sam_vendor_lookup_tab
from Scripts.streamlit_data_integration import render_data_integration_tab
from Scripts.stripe_billing_integration import render_stripe_billing_tab
from Scripts.admin_dashboard import render_admin_dashboard_tab

# Main marketing-style landing page

def render_landing_page():
    st.markdown("""
        <style>
        .hero {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: start;
            padding: 3rem 2rem;
        }
        .hero-text h1 {
            font-size: 3rem;
            font-weight: 800;
            color: #0f1e45;
            margin-bottom: 1rem;
        }
        .hero-text p {
            font-size: 1.125rem;
            color: #333;
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }
        .cta-button {
            padding: 0.75rem 2rem;
            background-color: #000;
            color: white;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .auth-box {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="top-nav" style="background:#0f1e45;padding:1rem 2rem;color:white;display:flex;justify-content:space-between;align-items:center;">
            <div style="font-weight:600;font-size:1.25rem;">PTW Intelligence Suite</div>
            <div>
                <a href="?page=auth&mode=login" style="color:white;margin-right:2rem;text-decoration:none;">Log in</a>
                <a href="?page=auth&mode=register" style="color:white;text-decoration:none;">Register</a>
            </div>
        </div>
        <div class="hero">
            <div class="hero-text">
                <h1>Price-to-Win Intelligence Suite</h1>
                <p>Turn data into decisions. Price smarter. Win faster.<br>
                Welcome to PTW Intelligence Suite.</p>
                <a href="?page=auth" class="cta-button">Get Started</a>
            </div>
            <div class="auth-box">
                <h3>Register</h3>
                <input type="text" placeholder="Email address" style="width:100%;padding:0.5rem;margin-top:1rem;" disabled>
                <input type="password" placeholder="Password" style="width:100%;padding:0.5rem;margin-top:1rem;" disabled>
                <button style="margin-top:1rem;padding:0.5rem 1rem;">Sign up</button>
                <p style="margin-top:1rem;font-size:0.9rem;">Already have an account? <a href="?page=auth&mode=login">Log in</a></p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Authorization page renderer with breadcrumb and instructions
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
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<a href='/?page=landing'>&larr; Back to Home</a>", unsafe_allow_html=True)
    st.markdown("<div class='auth-header'>Account Access</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='auth-instructions'>
        Please register or log in to access the PTW Intelligence Suite tools and analytics. If you don't have an account, select 'Register' to get started.
        </div>
    """, unsafe_allow_html=True)

    with st.container():
        streamlit_render_auth_page()

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

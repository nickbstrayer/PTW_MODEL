import streamlit as st

# Dummy user database for demo
def get_all_users():
    return [
        {"username": "admin", "email": "admin@example.com", "status": "active"},
        {"username": "nick", "email": "nick@example.com", "status": "unpaid"},
    ]

def render_admin_dashboard_tab():
    st.header("🔐 Admin Dashboard")
    st.markdown("Use this dashboard to manage users and view subscription status.")

    # List users
    st.subheader("📋 Registered Users")
    users = get_all_users()
    for user in users:
        col1, col2, col3 = st.columns([3, 4, 2])
        col1.write(user["username"])
        col2.write(user["email"])
        col3.write(f"Status: {user['status'].capitalize()}")

        # Optional admin actions
        with col3:
            if st.button(f"Revoke {user['username']}", key=f"revoke_{user['username']}"):
                st.success(f"✅ Revoked {user['username']} (demo only)")
            if st.button(f"Mark Unpaid {user['username']}", key=f"unpaid_{user['username']}"):
                st.warning(f"⚠️ Marked {user['username']} as unpaid (demo only)")

    st.markdown("---")
    st.info("🧪 This is a demo dashboard. Replace with database integration for production.")

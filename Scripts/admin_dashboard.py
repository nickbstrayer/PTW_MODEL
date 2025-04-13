import streamlit as st
import json
from pathlib import Path

USER_DB = Path("users.json")


def load_users():
    if USER_DB.exists():
        with open(USER_DB, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=2)

def render_admin_dashboard():
    st.title("🛡️ Admin Dashboard")

    # Security check (only allow admin emails)
    allowed_admins = ["ncbudhai@gmail.com"]  # Add more admins here
    if "user" not in st.session_state or st.session_state.user not in allowed_admins:
        st.warning("🚫 Access Denied: Admins only")
        return

    users = load_users()

    st.subheader("📋 Registered Users")

    if not users:
        st.info("No users found.")
        return

    for email, data in users.items():
        col1, col2, col3, col4 = st.columns([4, 2, 2, 2])
        with col1:
            st.text(email)
        with col2:
            paid_status = "✅ Paid" if data.get("paid") else "❌ Free"
            st.text(paid_status)
        with col3:
            if not data.get("paid"):
                if st.button(f"Mark Paid ({email})"):
                    users[email]["paid"] = True
                    save_users(users)
                    st.success(f"✔️ {email} marked as paid.")
                    st.experimental_rerun()
        with col4:
            if data.get("paid"):
                if st.button(f"Revoke Access ({email})"):
                    users[email]["paid"] = False
                    save_users(users)
                    st.warning(f"🚫 Access revoked for {email}.")
                    st.experimental_rerun()

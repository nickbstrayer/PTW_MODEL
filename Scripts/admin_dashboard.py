import streamlit as st
import pandas as pd

# Sample placeholder admin table data
USERS_DB = pd.DataFrame([
    {"username": "admin", "email": "admin@example.com", "role": "admin", "status": "active"},
    {"username": "demo", "email": "demo@example.com", "role": "user", "status": "unpaid"},
    {"username": "tester", "email": "tester@example.com", "role": "user", "status": "active"},
])

def render_admin_dashboard_tab():
    st.header("🔐 Admin Dashboard")

    st.markdown("Manage registered users and application access.")

    with st.expander("📋 View All Users"):
        st.dataframe(USERS_DB, use_container_width=True)

    with st.expander("✏️ Update User Status"):
        selected_user = st.selectbox("Select user to update", USERS_DB["username"])
        new_status = st.selectbox("Set new status", ["active", "unpaid", "revoked"])
        if st.button("Update Status"):
            USERS_DB.loc[USERS_DB["username"] == selected_user, "status"] = new_status
            st.success(f"Updated {selected_user}'s status to {new_status}.")

    with st.expander("➕ Add New User (Simulation)"):
        new_username = st.text_input("Username")
        new_email = st.text_input("Email")
        new_role = st.selectbox("Role", ["user", "admin"])
        if st.button("Add User"):
            if new_username and new_email:
                new_row = {"username": new_username, "email": new_email, "role": new_role, "status": "active"}
                USERS_DB.loc[len(USERS_DB)] = new_row
                st.success("User added (simulated only – no DB persistence).")
            else:
                st.warning("Please provide both username and email.")

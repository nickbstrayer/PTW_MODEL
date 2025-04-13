import streamlit as st

def render_auth_page():
    st.title("🔐 PTW Intelligence Suite Login")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        st.subheader("Sign in to your account")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            if email and password:
                st.success(f"Welcome back, {email}!")
            else:
                st.warning("Please fill in all fields.")

    with tab2:
        st.subheader("Create a new account")
        new_email = st.text_input("Email", key="reg_email")
        new_password = st.text_input("Password", type="password", key="reg_pass")
        confirm_password = st.text_input("Confirm Password", type="password", key="reg_pass2")

        if st.button("Register"):
            if not new_email or not new_password or not confirm_password:
                st.warning("All fields are required.")
            elif new_password != confirm_password:
                st.error("Passwords do not match.")
            else:
                st.success(f"Account registered for {new_email}!")
                # Placeholder for DB logic

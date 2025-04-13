import streamlit as st
import stripe
import os

# Load Stripe API key from Streamlit secrets
STRIPE_SECRET_KEY = st.secrets.get("STRIPE_SECRET_KEY", None)
stripe.api_key = STRIPE_SECRET_KEY if STRIPE_SECRET_KEY else ""

# Example product/price ID from Stripe dashboard (replace with your own)
PRODUCT_PRICE_ID = st.secrets.get("STRIPE_PRICE_ID", "price_1234_test")

# Simulated user ID or email from session (for testing)
def get_current_user():
    return st.session_state.get("user_email", "testuser@example.com")

def render_stripe_billing_tab():
    st.subheader("💳 Billing & Subscription")

    if not STRIPE_SECRET_KEY or STRIPE_SECRET_KEY == "":
        st.warning("Stripe API key not set. Billing is disabled in this environment.")
        st.markdown("To enable billing, add `STRIPE_SECRET_KEY` to Streamlit Secrets.")
        return

    user_email = get_current_user()

    st.markdown(f"**Logged in as:** `{user_email}`")

    # Option to subscribe
    if st.button("Subscribe for $29/month"):
        try:
            # Create a Stripe Checkout Session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': PRODUCT_PRICE_ID,
                    'quantity': 1,
                }],
                mode='subscription',
                customer_email=user_email,
                success_url='https://your-success-url.com',
                cancel_url='https://your-cancel-url.com',
            )
            st.success("Checkout session created.")
            st.markdown(f"[Click here to complete payment]({checkout_session.url})")
        except Exception as e:
            st.error(f"Error creating Stripe session: {e}")

    # Admin-only view (toggle with session_state)
    if st.session_state.get("is_admin", False):
        st.markdown("---")
        st.markdown("### 🔐 Admin Controls")
        st.markdown("This section is only visible to admins.")
        st.text_input("Lookup email", key="billing_lookup")
        st.button("Revoke Subscription (Simulated)")

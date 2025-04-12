import pandas as pd
import streamlit as st
from Scripts.gsa_fpds_data_pull import fetch_gsa_calc_rates, fetch_fpds_contracts
import io


def render_data_integration_tab():
    st.header("📈 Data Integration – PTW Intelligence Feed")

    # --- GSA CALC ---
    st.subheader("🔍 GSA CALC Rate Lookup")
    labor_input = st.text_input("Enter Labor Category", "Program Manager")
    gsa_data = pd.DataFrame()

    if st.button("Fetch GSA Rates"):
        gsa_data = fetch_gsa_calc_rates(labor_input)
        if not gsa_data.empty:
            st.dataframe(gsa_data)
            csv = gsa_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download GSA Data as CSV",
                data=csv,
                file_name=f"gsa_rates_{labor_input.replace(' ', '_')}.csv",
                mime='text/csv'
            )
        else:
            st.warning("No data found from GSA CALC.")

    # --- FPDS Feed ---
    st.subheader("📦 FPDS.gov Contract History")
    keyword_input = st.text_input("Enter FPDS Search Keyword", "Cybersecurity")
    fpds_data = pd.DataFrame()

    if st.button("Fetch FPDS Contracts"):
        fpds_data = fetch_fpds_contracts(keyword_input)
        if not fpds_data.empty:
            st.dataframe(fpds_data)
            csv = fpds_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download FPDS Results as CSV",
                data=csv,
                file_name=f"fpds_{keyword_input.replace(' ', '_')}.csv",
                mime='text/csv'
            )
        else:
            st.warning("No FPDS records found for this keyword.")

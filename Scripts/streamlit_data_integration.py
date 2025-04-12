import streamlit as st
import pandas as pd
from Scripts.gsa_fpds_data_pull import fetch_gsa_calc_rates, fetch_fpds_contracts

def render_data_integration_tab():
    st.header("🔍 GSA CALC Rate Lookup")

    labor_input = st.text_input("Enter Labor Category", "Program Manager")
    if st.button("Fetch GSA Rates"):
        rates = fetch_gsa_calc_rates(labor_input)
        if not rates.empty:
            st.dataframe(rates)
            st.download_button("📥 Download GSA Data as CSV", rates.to_csv(index=False), file_name="gsa_rates.csv")
        else:
            st.warning("No matching labor category found. Please refine your input.")

    st.markdown("---")

    st.header("📦 FPDS.gov Contract History")
    keyword_input = st.text_input("Enter FPDS Search Keyword", "Cybersecurity")
    if st.button("Fetch FPDS Contracts"):
        contracts = fetch_fpds_contracts(keyword_input)
        if not contracts.empty:
            st.dataframe(contracts)
            st.download_button("📥 Download FPDS Data as CSV", contracts.to_csv(index=False), file_name="fpds_contracts.csv")
        else:
            st.warning("No contracts found for this keyword. Try a different term.")

    st.info("This feature integrates public data to support PTW analytics.")

import streamlit as st
import pandas as pd
from difflib import get_close_matches
from Scripts.gsa_fpds_data_pull import fetch_gsa_calc_rates, fetch_fpds_contracts
import matplotlib.pyplot as plt

# Predefined list of known labor categories
KNOWN_LABOR_CATEGORIES = [
    "Program Manager", "Data Scientist", "Systems Engineer",
    "Cybersecurity Analyst", "Project Manager", "Logistics Analyst",
    "Database Administrator", "Network Engineer", "Help Desk Technician"
]

def render_data_integration_tab():
    st.header("🔍 GSA CALC Rate Lookup")

    input_text = st.text_input("Enter Labor Category (fuzzy match enabled)", "Cybersecurity Analyst")
    matched = get_close_matches(input_text, KNOWN_LABOR_CATEGORIES, n=1, cutoff=0.6)

    if st.button("Fetch GSA Rates"):
        if matched:
            st.success(f"Matched to: {matched[0]}")
            gsa_data = fetch_gsa_calc_rates(matched[0])
            df = pd.DataFrame(gsa_data)
            st.dataframe(df)

            if not df.empty:
                # Visualization
                st.subheader("📊 Rate Trend Over Time")
                fig, ax = plt.subplots()
                ax.plot(df["Year"], df["Hourly Rate"], marker='o', linestyle='-')
                ax.set_xlabel("Year")
                ax.set_ylabel("Hourly Rate ($)")
                ax.set_title(f"Hourly Rate Trend – {matched[0]}")
                ax.grid(True)
                st.pyplot(fig)

                # CSV Download
                st.download_button("Download CSV", df.to_csv(index=False), file_name="gsa_rates.csv")
        else:
            st.warning("No close match found. Please refine your labor category input.")

    st.markdown("---")
    st.header("📦 FPDS.gov Contract History")
    keyword = st.text_input("Enter FPDS Search Keyword", "Cybersecurity")
    if st.button("Fetch FPDS Contracts"):
        fpds_df = fetch_fpds_contracts(keyword)
        if not fpds_df.empty:
            st.dataframe(fpds_df)
            st.download_button("Download FPDS Data as CSV", fpds_df.to_csv(index=False), file_name="fpds_contracts.csv")
        else:
            st.warning("No results found for that keyword.")

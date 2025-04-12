import streamlit as st
import pandas as pd
from Scripts.sam_api_integration import fetch_sam_vendor_info

def render_sam_vendor_lookup_tab():
    st.header("🔎 SAM.gov Vendor Lookup")

    search_term = st.text_input("Enter Vendor Name or Keyword", "The MAASAI Group")
    if st.button("Search SAM.gov"):
        results = fetch_sam_vendor_info(search_term)
        st.dataframe(results)

        if not results.empty:
            csv = results.to_csv(index=False)
            st.download_button(
                label="📥 Download Vendor Info as CSV",
                data=csv,
                file_name=f"sam_vendor_lookup_{search_term.replace(' ', '_')}.csv",
                mime='text/csv'
            )
        else:
            st.warning("No data returned from SAM.gov for your query.")
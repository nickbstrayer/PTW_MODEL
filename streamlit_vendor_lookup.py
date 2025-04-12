import streamlit as st
import requests
import pandas as pd

def render_sam_vendor_lookup_tab():
    st.header("🔎 SAM.gov Vendor Lookup")

    query = st.text_input("Enter Vendor Name or Keyword", "")

    if st.button("Search SAM.gov") and query:
        with st.spinner("Searching SAM.gov..."):
            results = fetch_sam_vendors(query)
            if results:
                st.success(f"Found {len(results)} result(s).")
                df = pd.DataFrame(results)
                st.dataframe(df)
                st.download_button("⬇ Download CSV", df.to_csv(index=False), "sam_results.csv")
            else:
                st.warning("No matching vendors found.")

def fetch_sam_vendors(keyword):
    api_key = st.secrets["SAM_API_KEY"]
    url = f"https://api.sam.gov/entity-information/v2/entities?name={keyword}&api_key={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        matches = []
        for entity in data.get("entities", []):
            matches.append({
                "Legal Name": entity.get("entity", {}).get("legalBusinessName"),
                "UEI": entity.get("entity", {}).get("uei"),
                "CAGE": entity.get("entity", {}).get("cage"),
                "NAICS": ", ".join(entity.get("entity", {}).get("naicsList", [])),
                "Business Types": ", ".join(entity.get("entity", {}).get("businessTypes", [])),
            })

        return matches

    except Exception as e:
        st.error(f"Error fetching SAM data: {e}")
        return []

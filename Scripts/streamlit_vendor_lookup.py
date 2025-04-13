import streamlit as st
import requests

API_KEY = st.secrets["SAM_API_KEY"]
BASE_URL = "https://api.sam.gov/entity-information/v2/entities"

def render_sam_vendor_lookup_tab():
    st.header("SAM Vendor Lookup")

    search_mode = st.radio("Search by:", ["CAGE Code / UEI", "Vendor Name"])
    query = st.text_input("Enter CAGE Code / UEI" if search_mode == "CAGE Code / UEI" else "Enter Vendor Name")

    if query:
        st.info(f"Looking up SAM.gov data for: {query}")
        
        try:
            params = {"api_key": API_KEY}
            if search_mode == "CAGE Code / UEI":
                params["cageCode"] = query.upper()
            else:
                params["legalBusinessName"] = query

            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if response.status_code == 200:
                if "entities" in data and len(data["entities"]) > 0:
                    for key, value in data["entities"][0].items():
                        st.write(f"**{key}:** {value}")
                else:
                    st.warning("No matching records found.")
            else:
                error = data.get("error", {})
                st.error(f"❌ Forbidden: {error.get('message', 'Unknown error')}")
                st.code(data, language="json")

        except Exception as e:
            st.error("An error occurred during the lookup.")
            st.exception(e)

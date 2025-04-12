import streamlit as st
import requests

# Retrieve the API key securely from Streamlit Secrets
API_KEY = st.secrets["SAM_API_KEY"]

# Function to call SAM.gov API
def search_sam_gov(search_type, query):
    headers = {
        "Accept": "application/json",
        "X-API-KEY": API_KEY
    }

    if search_type == "Vendor Name":
        url = "https://api.sam.gov/entity-information/v2/entities"
        params = {"name": query}
    else:  # CAGE or UEI
        if len(query) > 5:
            params = {"ueiSAM": query}
        else:
            params = {"cageCode": query}
        url = "https://api.sam.gov/entity-information/v2/entities"

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        st.error("❌ Error retrieving data from SAM.gov. Please check the key or query format.")
        st.text(str(err))
        return None

# Streamlit UI
def render_sam_vendor_lookup_tab():
    st.header("SAM Vendor Lookup")

    search_type = st.radio("Search by:", ["CAGE Code / UEI", "Vendor Name"])
    query = st.text_input("Enter CAGE Code / UEI" if search_type == "CAGE Code / UEI" else "Enter Vendor Name")

    if query:
        st.info(f"Looking up SAM.gov data for: {query}")
        data = search_sam_gov(search_type, query)

        if data and data.get("entities"):
            entity = data["entities"][0]  # First matched entity
            st.write("**Legal Business Name:**", entity.get("legalBusinessName", "N/A"))
            st.write("**UEI:**", entity.get("ueiSAM", "N/A"))
            st.write("**CAGE Code:**", entity.get("cageCode", "N/A"))
            st.write("**Status:**", entity.get("status", {}).get("status", "N/A"))
            st.write("**City:**", entity.get("address", {}).get("city", "N/A"))
            st.write("**State:**", entity.get("address", {}).get("stateOrProvince", "N/A"))
            st.write("**Country:**", entity.get("address", {}).get("countryCode", "N/A"))
        elif data:
            st.warning("No matching vendor found. Please refine your input or try a different search method.")
        else:
            st.error("An error occurred during the lookup. Check your API key or connection.")

import streamlit as st
import requests
import difflib

SAM_API_KEY = "YOUR_SAM_API_KEY_HERE"  # Replace or read from env var

def render_sam_vendor_lookup_tab():
    st.header("SAM Vendor Lookup")

    search_mode = st.radio("Search by:", ["CAGE Code / UEI", "Vendor Name"])

    if search_mode == "CAGE Code / UEI":
        query = st.text_input("Enter CAGE Code or UEI")
    else:
        query = st.text_input("Enter Vendor Name")

    if query:
        st.info(f"Looking up SAM.gov data for: {query}")

        if search_mode == "Vendor Name":
            endpoint = f"https://api.sam.gov/entity-information/v2/entities?name={query}&api_key={SAM_API_KEY}"
        else:
            endpoint = f"https://api.sam.gov/entity-information/v2/entities/{query}?api_key={SAM_API_KEY}"

        response = requests.get(endpoint)

        if response.status_code == 200:
            data = response.json()
            entities = data.get("entityInformation", [])

            if not entities:
                st.warning("No vendor match found. Try another name.")
            else:
                best_match = entities[0]
                display_vendor_info(best_match)

        else:
            st.error("Error retrieving data from SAM.gov. Please check the key or query format.")

def display_vendor_info(entity):
    name = entity.get("legalBusinessName", "N/A")
    uei = entity.get("uei", "N/A")
    cage = entity.get("cageCode", "N/A")
    status = entity.get("status", {}).get("status", "N/A")
    city = entity.get("mailingAddress", {}).get("city", "N/A")
    state = entity.get("mailingAddress", {}).get("stateOrProvince", "N/A")
    country = entity.get("mailingAddress", {}).get("countryCode", "N/A")

    st.markdown(f"**Legal Business Name:** {name}")
    st.markdown(f"**UEI:** {uei}")
    st.markdown(f"**CAGE Code:** {cage}")
    st.markdown(f"**Status:** {status}")
    st.markdown(f"**City:** {city}")
    st.markdown(f"**State:** {state}")
    st.markdown(f"**Country:** {country}")

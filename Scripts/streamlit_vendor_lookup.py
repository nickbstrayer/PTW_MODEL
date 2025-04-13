import streamlit as st
import requests
import urllib.parse

API_KEY = st.secrets["SAM_API_KEY"]

def render_sam_vendor_lookup_tab():
    st.header("SAM Vendor Lookup")

    search_type = st.radio("Search by:", ["CAGE Code / UEI", "Vendor Name"])
    
    if search_type == "CAGE Code / UEI":
        query_value = st.text_input("Enter CAGE Code or UEI").strip()
        query_param = "cageCode"
    else:
        query_value = st.text_input("Enter Vendor Name").strip()
        query_param = "name"

    if query_value:
        if query_param == "name":
            # Add wildcard (*) and URL-encode it
            query_value = urllib.parse.quote_plus(query_value + "*")
        else:
            query_value = urllib.parse.quote_plus(query_value)

        query_url = (
            f"https://api.sam.gov/entity-information/v2/entities?"
            f"{query_param}={query_value}&api_key={API_KEY}"
        )

        st.info(f"Looking up SAM.gov data for: {urllib.parse.unquote_plus(query_value)}")

        try:
            response = requests.get(query_url)
            data = response.json()

            if response.status_code == 200 and "entityData" in data and data["entityData"]:
                entity = data["entityData"][0]
                for key, value in entity.items():
                    st.write(f"**{key}:** {value}")
            elif "error" in data:
                st.error(f"❌ {data['error'].get('message', 'Unknown API error')}")
                st.code(data, language="json")
            else:
                st.warning("No results found. Try refining your search.")
        except Exception as e:
            st.error("⚠️ An error occurred during the lookup. Check your API key or connection.")
            st.exception(e)

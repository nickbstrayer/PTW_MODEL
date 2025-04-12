import streamlit as st
import requests

API_KEY = st.secrets["SAM_API_KEY"]

def render_sam_vendor_lookup_tab():
    st.header("SAM Vendor Lookup")

    search_by = st.radio("Search by:", ["CAGE Code / UEI", "Vendor Name"])
    user_input = st.text_input(f"Enter {search_by}").strip()

    if user_input:
        st.info(f"Looking up SAM.gov data for: {user_input}")

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        if search_by == "CAGE Code / UEI":
            url = f"https://api.sam.gov/entity-information/v2/entities?cageCode={user_input}"
        else:
            url = f"https://api.sam.gov/entity-information/v2/entities?name={user_input}"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 403:
                st.error("❌ Forbidden: Your API key may be invalid or access is restricted.")
                st.code(response.text)
                return
            elif response.status_code != 200:
                st.error(f"❌ Error retrieving data. Status code: {response.status_code}")
                st.code(response.text)
                return

            data = response.json()
            entities = data.get("entities", [])

            if not entities:
                st.warning("⚠️ No results found. Try refining your search.")
                return

            vendor = entities[0]  # just show the first result

            fields = {
                "Legal Business Name": vendor.get("legalBusinessName"),
                "UEI": vendor.get("ueiSAM"),
                "CAGE Code": vendor.get("cageCode"),
                "Status": vendor.get("entityStatus", {}).get("entityStatus"),
                "City": vendor.get("physicalAddress", {}).get("city"),
                "State": vendor.get("physicalAddress", {}).get("stateOrProvince"),
                "Country": vendor.get("physicalAddress", {}).get("countryCode")
            }

            for key, value in fields.items():
                if value:
                    st.write(f"**{key}:** {value}")

        except Exception as e:
            st.error("An error occurred during the lookup. Check your API key or connection.")
            st.exception(e)

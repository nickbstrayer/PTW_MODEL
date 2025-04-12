import streamlit as st

# Simulated vendor directory (placeholder for actual API query results)
vendor_directory = {
    "5T2B3": {
        "Legal Business Name": "Acme Federal Services LLC",
        "UEI": "ABCD12345678",
        "CAGE Code": "5T2B3",
        "Status": "Active",
        "City": "Washington",
        "State": "DC",
        "Country": "USA"
    },
    "8J7K2": {
        "Legal Business Name": "Defense Solutions Inc.",
        "UEI": "EFGH98765432",
        "CAGE Code": "8J7K2",
        "Status": "Inactive",
        "City": "Arlington",
        "State": "VA",
        "Country": "USA"
    }
}

def render_sam_vendor_lookup_tab():
    st.header("SAM Vendor Lookup")
    search_type = st.radio("Search by", ["CAGE/UEI", "Vendor Name"])

    query = st.text_input(f"Enter {search_type}").strip().upper()

    if query:
        st.info(f"Looking up SAM.gov data for: {query}")
        result = None

        # Lookup by CAGE or UEI
        if search_type == "CAGE/UEI":
            for data in vendor_directory.values():
                if data["CAGE Code"] == query or data["UEI"] == query:
                    result = data
                    break

        # Lookup by Vendor Name
        elif search_type == "Vendor Name":
            for data in vendor_directory.values():
                if query in data["Legal Business Name"].upper():
                    result = data
                    break

        # Display result or suggestions
        if result:
            for key, value in result.items():
                st.write(f"**{key}:** {value}")
        else:
            st.warning("No exact match found.")
            st.markdown("### 🔍 Try one of the following suggestions:")
            for data in vendor_directory.values():
                st.write(f"- **{data['Legal Business Name']}** (CAGE: {data['CAGE Code']}, UEI: {data['UEI']})")

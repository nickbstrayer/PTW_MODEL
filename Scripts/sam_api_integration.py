import requests
import pandas as pd

SAM_API_KEY = "f2gGlBlN4L8Q9HzeXyHHTvvNwkvz3m7OIxhFMDhu"

def fetch_sam_vendor_info(search_term, limit=1):
    base_url = "https://api.sam.gov/entity-information/v2/entities"
    params = {
        "api_key": SAM_API_KEY,
        "q": search_term,
        "limit": limit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        results = response.json().get("entities", [])

        if not results:
            return pd.DataFrame([{"Search Term": search_term, "Message": "No results found"}])

        # Extract useful fields
        data = []
        for entity in results:
            data.append({
                "Legal Business Name": entity.get("legalBusinessName"),
                "UEI": entity.get("uei"),
                "CAGE Code": entity.get("cageCode"),
                "DUNS": entity.get("duns"),
                "NAICS Codes": ", ".join(entity.get("naicsCodes", [])),
                "Status": entity.get("status", {}).get("status"),
                "Business Types": ", ".join(entity.get("businessTypes", []))
            })

        return pd.DataFrame(data)

    except requests.RequestException as e:
        return pd.DataFrame([{"Search Term": search_term, "Error": str(e)}])
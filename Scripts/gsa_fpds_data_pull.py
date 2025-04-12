import pandas as pd

def fetch_gsa_calc_rates(labor_category):
    # Simulated response — replace with real scraping or API if needed
    data = [
        {"Labor Category": labor_category, "Year": 2023, "Hourly Rate": 115.25},
        {"Labor Category": labor_category, "Year": 2022, "Hourly Rate": 112.75},
        {"Labor Category": labor_category, "Year": 2021, "Hourly Rate": 109.50},
    ]
    return pd.DataFrame(data)

def fetch_fpds_contracts(keyword):
    # Simulated contract history — replace with real FPDS pull
    data = [
        {"Award ID": "W91QF0-23-C-1234", "Vendor": "ABC Corp", "Award Amount": 4750000, "NAICS": "541512", "Keyword": keyword},
        {"Award ID": "N65236-22-D-0022", "Vendor": "XYZ Inc", "Award Amount": 2230000, "NAICS": "541511", "Keyword": keyword},
    ]
    return pd.DataFrame(data)
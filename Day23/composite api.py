import requests
import json

# Expected fields in the API response
EXPECTED_FIELDS = ["latitude", "longitude", "hourly"]

def validate_response(response):
    """Validate response status, completeness, expected fields."""
    result = {
        "status_code_valid": False,
        "fields_valid": False,
        "data_complete": False,
        "errors": [],
        "data": None
    }

    # 1. Check correct status code
    if response.status_code == 200:
        result["status_code_valid"] = True
    else:
        result["errors"].append(f"Invalid status code: {response.status_code}")
        return result  # no need to continue

    # Convert JSON into Python dictionary
    try:
        data = response.json()
        result["data"] = data
    except Exception as e:
        result["errors"].append(f"JSON decode failed: {str(e)}")
        return result

    # 2. Validate expected fields
    missing_fields = [field for field in EXPECTED_FIELDS if field not in data]
    if missing_fields:
        result["errors"].append(f"Missing fields: {missing_fields}")
    else:
        result["fields_valid"] = True

    # 3. Check completeness (wave_height data exists)
    try:
        wave_data = data["hourly"]["wave_height"]
        if isinstance(wave_data, list) and len(wave_data) > 0:
            result["data_complete"] = True
        else:
            result["errors"].append("wave_height is empty")
    except:
        result["errors"].append("wave_height missing or invalid")

    return result


# API URLs
url1 = "https://marine-api.open-meteo.com/v1/marine?latitude=13.3347&longitude=74.7462&hourly=wave_height"
url2 = "https://marine-api.open-meteo.com/v1/marine?latitude=17.6801&longitude=83.2016&hourly=wave_height"

# Make API calls
response1 = requests.get(url1)
response2 = requests.get(url2)

# Validate both responses
validated1 = validate_response(response1)
validated2 = validate_response(response2)

# Merge results into a single aggregate JSON
final_output = {
    "location_1": validated1,
    "location_2": validated2
}

# Save final aggregated output
with open("aggregate_output.json", "w") as file:
    file.write(json.dumps(final_output, indent=4))
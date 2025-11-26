import yaml
import json

# Open the YAML file
with open("TS24560_Aimlec_AIMLEClientServiceOperations.yaml", "r") as f:
    data = yaml.safe_load(f)

# Write data into a new JSON file
with open("output.json", "w") as jf:
    json.dump(data, jf, indent=4)

print("Conversion completed: YAML → JSON saved as output.json")

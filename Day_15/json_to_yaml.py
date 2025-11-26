import json
import yaml

# Open JSON file
with open("sample2.json", "r") as f:
    data = json.load(f)

# Convert to YAML
yaml_data = yaml.safe_dump(data, default_flow_style=False)

# Save to YAML file
with open("output.yaml", "w") as yf:
    yf.write(yaml_data)

print("Conversion completed: JSON → YAML saved as output.yaml")

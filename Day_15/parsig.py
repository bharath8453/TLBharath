import json
import yaml

with open("TS24560_Aimlec_AIMLEClientServiceOperations.yaml") as f:
    data = yaml.safe_load(f)

print(data)

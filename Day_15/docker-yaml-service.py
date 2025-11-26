import yaml

with open("docker-compose-basic-nrf.yaml") as f:
    data = yaml.safe_load(f)

services = data.get("services", {})

service_ips = {}
service_dependencies = {}
service_ports = {}

for service_name, service_data in services.items():

    # -------------------------
    # 1. Extract IP Address
    # -------------------------
    ip_address = None
    networks = service_data.get("networks", {})
    for net_name, net_data in networks.items():
        if "ipv4_address" in net_data:
            ip_address = net_data["ipv4_address"]
    service_ips[service_name] = ip_address

    # -------------------------
    # 2. Extract Dependencies
    # -------------------------
    depends_on = service_data.get("depends_on", [])
    if isinstance(depends_on, dict):
        depends_on = list(depends_on.keys())
    service_dependencies[service_name] = depends_on

    # -------------------------
    # 3. Extract NRF_PORT
    # -------------------------
    nf_port = None
    env_vars = service_data.get("environment", [])
    for entry in env_vars:
        if entry.startswith("NRF_PORT="):
            nf_port = entry.split("=", 1)[1]
            break
    service_ports[service_name] = nf_port

print("\n=== Service → IP Address ===")
for svc, ip in service_ips.items():
    print(f"{svc}: {ip}")

print("\n=== Service → Dependencies ===")
for svc, deps in service_dependencies.items():
    print(f"{svc}: {deps}")

print("\n=== Service → NRF_PORT ===")
for svc, port in service_ports.items():
    print(f"{svc}: {port}")


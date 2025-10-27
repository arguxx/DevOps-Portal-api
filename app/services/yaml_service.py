import yaml

def generate_deployment(data):
    name = data.get('name')
    image = data.get('image')
    tier = data.get('tier')
    namespace = data.get('namespace')
    port = data.get('ports')
    action = data.get('action') 

    if isinstance(port, str):
        ports = [p.strip() for p in port.split(",") if p.strip()]
    elif isinstance(port, list):
        ports = [str(p).strip() for p in port if str(p).strip()]
    else:
        ports = None

    try:
        container_ports = [{"containerPort": int(p)} for p in ports] if ports else None
    except ValueError:
        raise ValueError("Ports must be valid integers.")

    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": name},
        "spec": {
            "selector": {"matchLabels": {"app": name}},
            "template": {
                "metadata": {"labels": {"app": name}},
                "spec": {
                    "containers": [
                        {"name": name, "image": image}
                    ]
                }
            }
        }
    }

    if namespace:
        deployment["metadata"]["namespace"] = namespace
    if tier:
        deployment["spec"]["tier"] = int(tier)
    if container_ports:
        deployment["spec"]["template"]["spec"]["containers"][0]["ports"] = container_ports

    yaml_output = yaml.dump(deployment, sort_keys=False)
    # return f"<pre>{yaml_output}</pre>"

    if action == "generate":
        return yaml_output
    elif action == "print":
        return yaml_output
    
def generate_service(data):
    name = data.get('name')
    tier = data.get('tier')
    namespace = data.get('namespace')
    action = data.get('action') 
    port = data.get('port')
    target_port = data.get('targetPort')
    node_port = data.get('nodePort')

    try:
        port = int(port) if port else None
    except ValueError:
        raise ValueError("Port must be valid integers.")
    
    try:
        target_port = int(target_port) if target_port else None
    except ValueError:
        raise ValueError("Target Port must be valid integers.")

    service = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {
            "name": name,
            "tier": tier
            },
        "spec": {
            "selector": {
                "matchLabels": {
                    "app": name,
                    "tier": tier
                    }
                },
            "ports": [
                {
                    "name": "name",
                    "port": port,
                    "protocol": "TCP",
                    "targetPort": target_port,
                    "nodePort": node_port
                }
                ],
            "type": "NodePort"
            }
        }
    if namespace:
        service["metadata"]["namespace"] = namespace

    yaml_output = yaml.dump(service, sort_keys=False)
    if action == "generate":
        return yaml_output
    elif action == "print":
        return yaml_output



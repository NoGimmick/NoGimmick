import yaml

def load_environment():

    with open("app/context/environment.yaml", "r") as f:
        return yaml.safe_load(f)

def load_system_context():

    with open("app/context/system_context.txt", "r") as f:
        return f.read()
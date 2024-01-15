from template import Template
import json

def create(name="undefined", **kwargs) -> Template:
    template_dict = {
        "name": name,
        "inputFieldValues": kwargs.get("inputFieldValues", []),
        "resourceURLs": kwargs.get("resourceURLs", []),
        "mainValues": kwargs.get("mainValues", []),
        "constantValues": kwargs.get("constantValues", []),
        "functions": kwargs.get("functions", []),
    }
    template = Template(template_dict)
    return template

def load_from_json(file_path: str) -> Template:
    with open(file_path, "r") as file:
        data = json.load(file)
    return Template(data)

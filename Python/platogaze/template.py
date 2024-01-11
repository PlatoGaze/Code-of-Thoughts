import json
from function import Function


class Template:
    def __init__(self, template_json=None):
        self.template = {
            "name": "undefined",
            "api_key": "undefined",
            "chain_list": []
        }

        if template_json:
            self.from_json(template_json)

    def from_json(self, template_json):
        self.template["name"] = template_json.get("name", "undefined")
        self.template["api_key"] = template_json.get("api_key", "00000000")
        self.template["chain_list"] = [
            chain for chain in template_json.get("chain_list", [])]
    
    def add_function(self, new_func):
        self.template["chain_list"].append(new_func.to_dict())

    def save_to_json(self, file_path):
        with open(file_path, "w") as json_file:
            json.dump(self.template, json_file, indent=2)

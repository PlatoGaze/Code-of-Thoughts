import json
from chain import Chain

class Template:
    def __init__(self, template_dict=None):
        self.template = {
            "name": "",
            "api": "",
            "chain_list": []
        }

        if template_dict:
            self.from_dict(template_dict)

    def from_dict(self, template_dict):
        self.template["name"] = template_dict.get("name", "undefined")
        self.template["api"] = template_dict.get("api", "00000000")
        self.template["chain_list"] = [Chain(chain_dict = chain).chain for chain in template_dict.get("chain_list", [])]

    def save_to_json(self, file_path):
        with open(file_path, "w") as json_file:
            json.dump(self.template, json_file, indent=2)

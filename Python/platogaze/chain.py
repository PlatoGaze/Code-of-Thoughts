import json

class Chain:
    def __init__(self, chain_dict=None):
        self.chain = {
            "type": "",
            "display": False,
            "prompt": [],
            "reference_list": []
        }

        if chain_dict:
            self.from_dict(chain_dict)
    
    def from_dict(self, chain_dict):
        self.chain["type"] = chain_dict.get("type", "")
        self.chain["display"] = chain_dict.get("display", False)
        self.chain["prompt"] = chain_dict.get("prompt", [])
        self.chain["reference_list"] = chain_dict.get("reference_list", [])
    
    def set_type(self, chain_type):
        self.chain["type"] = chain_type

    def set_display(self, display):
        self.chain["display"] = display

    def add_prompt(self, prompt):
        self.chain["prompt"].append(prompt)

    def add_reference(self, ref_type, ref_prompt):
        reference = {
            "type": ref_type,
            "prompt": ref_prompt
        }
        self.chain["reference_list"].append(reference)

    def save_to_json(self, file_path):
        with open(file_path, "w") as json_file:
            json.dump(self.chain, json_file, indent=2)

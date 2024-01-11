import json

class Function:
    def __init__(self, chain_json=None):
        self.chain = {
            "type": "",
            "display": False,
            "prompt": [],
            "reference_list": []
        }

        if chain_json:
            self.from_dict(chain_json)
    
    def from_dict(self, func_json):
        self.chain["type"] = func_json.get("type", "")
        self.chain["display"] = func_json.get("display", False)
        self.chain["prompt"] = func_json.get("prompt", [])
        self.chain["reference_list"] = func_json.get("reference_list", [])
    
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
    
    def to_dict(self):
        return self.chain.copy()

import json

class Chain:
    def __init__(self):
        self.chain = {
            "type": "",
            "display": False,
            "prompt": [],
            "reference": []
        }

    def setType(self, chain_type):
        self.chain["type"] = chain_type

    def setDisplay(self, display):
        self.chain["display"] = display

    def addPrompt(self, prompt):
        self.chain["prompt"].append(prompt)

    def addReference(self, ref_type, ref_prompt):
        reference = {
            "type": ref_type,
            "prompt": ref_prompt
        }
        self.chain["reference"].append(reference)

    def saveToJson(self, file_path):
        with open(file_path, "w") as json_file:
            json.dump(self.chain, json_file, indent=2)

# Example usage:
chain = Chain()
chain.setType("standard")
chain.setDisplay(False)
chain.addPrompt("Write an essay about [0]. Use a [1] tone.")
chain.addReference("standard", "liberty")
chain.addReference("fixed", "serious")
chain.saveToJson("chain.json")

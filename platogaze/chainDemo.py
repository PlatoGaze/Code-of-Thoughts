import json

class ChainBuilder:
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
builder = ChainBuilder()
builder.setType("standard")
builder.setDisplay(False)
builder.addPrompt("Write an essay about [0]. Use a [1] tone.")
builder.addReference("standard", "liberty")
builder.addReference("fixed", "serious")
builder.saveToJson("chain.json")

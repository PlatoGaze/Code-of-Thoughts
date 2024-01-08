import requests
import time

class Agent:
    def __init__(self, template):
        self.template = template

    def fake_api_call(self, prompt):
        # This is a fake API call function. Replace it with a real API call when you have access.
        print(f"API called with prompt: {prompt}")
        # time.sleep(1)  # Simulate delay
        return "This is a fake response from the API."

    def execute(self):
        for chain in self.template.template["chain_list"]:
            prompt = chain["prompt"]
            response = self.fake_api_call(prompt)
            if chain["display"]:
                print(f"Response for prompt '{prompt}': {response}")
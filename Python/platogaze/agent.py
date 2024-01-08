class Agent:
    def __init__(self, template):
        self.template = template
        self.output_list = []

    def fake_api_call(self, prompt):
        # This is a fake API call function. Replace it with a real API call when you have access.
        print(f"API called with prompt: {prompt}")
        # time.sleep(1)  # Simulate delay
        return "This is a fake response from the API."

    def run(self):
        for ix, chain in enumerate(self.template.template["chain_list"]):
            print(f"Running chain: {ix}")
            prompt = chain["prompt"][0]
            # process prompt
            if (chain["reference_list"]):
                for jx, reference in enumerate(chain["reference_list"]):
                    prompt = prompt.replace(f"[{jx}]", str(chain["reference_list"][jx]["prompt"]))
            response = self.fake_api_call(prompt)
            if chain["display"]:
                print(f"Response for prompt '{prompt}': {response}")
            else:
                print(f"Display mode is turned off for chain {ix}")
            self.output_list.append(response)


import json
import sys
import os
sys.path.append(os.getcwd() + r"/python/src")
import platogaze

file_path = "python/tests/code.json"

# Load JSON data from file
with open(file_path, 'r') as file:
    script = json.load(file)

# Traverse the function starting from the root
platogaze.run(script["template"])  # template["template"] is a list of codes or expressions

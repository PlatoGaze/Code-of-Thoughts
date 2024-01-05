from template import Template
from chain import Chain
import json


file_path = "Python/platogaze/my_template.json"
with open(file_path, "r") as f:
    data = json.load(f)

test_template = Template(data)
test_template.save_to_json("saved_template.json")
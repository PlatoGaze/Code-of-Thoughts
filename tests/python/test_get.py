import sys
import os

sys.path.append(os.getcwd() + r"\python")
import platogaze

tempate_1_path = "test_template_1.json"

test_template_1 = platogaze.load_from_json(file_path="test_template_1.json")

test_template_1.get("1").display()
test_template_1.get("2").display()
# test_template_1.get("3").display()
test_template_1.get("1.1").display()
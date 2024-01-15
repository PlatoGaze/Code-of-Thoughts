import sys
import os

sys.path.append(os.getcwd() + r"\python")
import platogaze


tempate_1_path = "test_template_1.json"
tempate_2_path = "test_template_2.json"

test_template_1 = platogaze.create(name="test_template_1")
test_template_2 = platogaze.create(name="test_template_2")

print("test_template_1: ")
test_template_1.display()
print("test_template_2: ")
test_template_2.display()

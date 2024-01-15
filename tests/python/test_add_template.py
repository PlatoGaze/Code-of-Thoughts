import sys
import os

sys.path.append(os.getcwd() + r"\python")
import platogaze

path_1 = "test_template_1.json"
template_1 = platogaze.load_from_json(file_path=path_1)
print("template_1:")
template_1.display()

path_2 = "test_template_2.json"
template_2 = platogaze.load_from_json(file_path=path_2)
print("\ntemplate_2:")
template_2.display()

print("Add template 2 as the third code in template_1[\"functions\"]")
template_1.add_template(template_2)
print("\nnew template_1:")
template_1.display()
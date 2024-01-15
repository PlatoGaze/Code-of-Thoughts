import sys
import os

sys.path.append(os.getcwd() + r"\python")
import platogaze

test_tempate_1_path = "test_template_1.json"
test_template_1 = platogaze.load_from_json(file_path=test_tempate_1_path)
print("test_template_1:")
test_template_1.display()

test_tempate_2_path = "test_template_2.json"
test_template_2 = platogaze.load_from_json(file_path=test_tempate_2_path)
print("\ntest_template_2:")
test_template_2.display()

print("Add template 2 as the third code in template[\"functions\"]")
test_template_1.add_template(test_template_2)
print("\nnew test_template_1:")
test_template_1.display()
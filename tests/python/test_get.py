import sys
import os

sys.path.append(os.getcwd() + r"\python")
import platogaze

program_1_path = "test_program_1.json"

test_program_1 = platogaze.load_from_json(file_path="test_program_1.json")

test_program_1.get("1")["item"].display()
test_program_1.get("2")["item"].display()
# test_program_1.get("3")["item"].display()
# test_program_1.get("1.1").display()
# test_program_1.get("2.1").display()
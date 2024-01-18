import sys
import os

sys.path.append(os.getcwd() + r"\python")
import platogaze


program_1_path = "test_program_1.json"
program_2_path = "test_program_2.json"

test_program_1 = platogaze.create(name="test_program_1")
test_program_2 = platogaze.create(name="test_program_2")

print("test_program_1: ")
test_program_1.display()
print("test_program_2: ")
test_program_2.display()

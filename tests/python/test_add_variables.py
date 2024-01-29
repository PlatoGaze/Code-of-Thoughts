import sys
import os
sys.path.append(os.getcwd() + r"\python")
import platogaze
from platogaze import *


path = "test_program_1.json"
program = platogaze.load_from_json(file_path=path)
print("program_1:")
program.display()

# print("Add an input to program[\"variables\"]")
# program.add("variable", {"name": "animal", "value": "cat"}, "i")
# program.display()

print("Add an input to program[\"functions\"][0][\"program\"][\"variables\"]")
program.add("variable", {"name": "animal", "value": "dog"}, "i1")
program.display()

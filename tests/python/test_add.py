import sys
import os
sys.path.append(os.getcwd() + r"\python")
import platogaze
from platogaze import *


path_1 = "test_program_1.json"
program_1 = platogaze.load_from_json(file_path=path_1)
print("program_1:")
program_1.display()

path_2 = "test_program_2.json"
program_2 = platogaze.load_from_json(file_path=path_2)
print("\nprogram_2:")
program_2.display()

# 四个测试，分块注释了

# print("Add program 2 as the third program in program_1[\"functions\"]")
# program_1.add("program", program_2, "")
# print("\nnew program_1:")
# program_1.display()

# print("Add funtion to program 1 in the root path")
# print("Initialize the funtion")
# function_1 = Function({
#     "type": "standard",
#     "prompt": "Reference from input: [i0]",
#     "main": True,
#     "output_type": "string"
# })
# program_1.add("function", function_1, "")
# print("\nnew program_1:")
# program_1.display()

# print("Add program to program 1 [\"functions\"][0][\"program\"][\"functions\"]")
# program_1.add("program", program_2, "1")
# program_1.display()

# print("Add function to program 1 [\"functions\"][0][\"program\"][\"functions\"]")
# print("Initialize the funtion")
# function_1 = Function({
#     "type": "standard",
#     "prompt": "Hitman is so awesome!",
#     "main": True,
#     "output_type": "string"
# })
# program_1.add("function", function_1, "1")
# print("\nnew program_1:")
# program_1.display()



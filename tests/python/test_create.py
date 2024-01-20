import sys
import os

sys.path.append(os.getcwd() + r"\python")
import platogaze

# create a program
program = platogaze.create("program", {"name": "test_program_1"})
print("test_program_1: ")
program.display()

# create a function
function = platogaze.create("function", {
    "prompt": "This is a test function",
    "output_type": "string"
})
print("test_function_1: ")
function.display()

# create a variable
variable = platogaze.create("variable", {
    "name": "test_variable_1",
    "value": "test_value_1"
})
print("test_variable_1: ")
print(variable)
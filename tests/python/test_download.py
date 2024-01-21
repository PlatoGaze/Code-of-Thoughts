import sys
import os
import json
sys.path.append(os.getcwd() + r"\python")
import platogaze
from platogaze import *

program_1 = platogaze.create("program", {
    "name": "program_1",
})
program_1.display()

function_1 = platogaze.create("function", {
    "prompt": "Oh mighty god!"
})
function_1.display()

program_1.add("function", function_1)
program_1.display()

function_2 = platogaze.create("function", {
    "prompt": "What's your name?"
})
program_1.add("function", function_2)
program_1.display()

program_2 = platogaze.create("program", {
    "name": "program_2",
})
program_2.add("function", function_1)
program_2.add("program", program_1)
program_2.add("function", function_2)
program_2.display()

program_2.add("variable", {
    "name": "variable_1",
    "value": 1
},"i")
program_2.display()

# deeper level
program_2.add("function", function_1, "2")
program_2.display()
program_2.add("program", program_1, "2")
program_2.display()
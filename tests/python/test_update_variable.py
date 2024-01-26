import sys
import os
sys.path.append(os.getcwd() + r"\python")
from platogaze import Program, Function
import platogaze

path_1 = "test_program_1.json"
program_1 = platogaze.load_from_json(file_path=path_1)
print("program_1:")
program_1.display()

program_2 = Program({
    "name": "DNA program",
    "variables": [
        {
            "id": 1,
            "type": "input",
            "name": "uncle",
            "value": "Sam"
        }
    ],
    "functions": [
        {
            "id": 1,
            "type": "standard",
            "main": True,
            "prompt": "Bro, that is DNA!",
            "output_type": "string"
        }
    ]
})

print("program_2:")
program_2.display()

print('Update program_2\'s first variable')
program_2.update("variable", {
    "name": "grandpa", "value": "Joe"
}, "i1")
print("new program_2")
program_2.display()

print('Update program["functions"][0]["program"]["variables][0] as grandpa Joe')
program_1.update("variable", {
    "name": "grandpa", "value": "Joe"
}, "i1.1")
print("new program_1")
program_1.display()
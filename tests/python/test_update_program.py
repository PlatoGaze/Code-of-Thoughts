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

print('Update program_1["functions][0] as program_2')
program_1.update("program", program_2, "1")
print("new program_1")
program_1.display()
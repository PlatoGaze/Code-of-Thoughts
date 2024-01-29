import python.platogaze as pl
import json

# 假设 JSON 数据存储在 'data.json' 文件中
filename = "test_program_1.json"

program_dict = {
    "name": "test_program_1",
    "variables": [
        {"id": 1, "name": "country", "type": "input", "value": "china"},
        {"id": 2, "name": "google", "type": "url", "value": "www.google.com"},
    ],
    "functions": [
        {
            "id": 1,
            "type": "program",
            "program": {
                "name": "test_program_2",
                "variables": [
                    {"id": 1, "name": "country", "type": "input", "value": "china"},
                    {
                        "id": 2,
                        "name": "google",
                        "type": "url",
                        "value": "www.google.com",
                    },
                ],
                "functions": [
                    {
                        "id": 1,
                        "type": "standard",
                        "main": True,
                        "prompt": "Reference from main [country]",
                        "output_type": "string",
                        "name": "fun1",
                    }
                ],
            },
        },
        {
            "id": 2,
            "type": "standard",
            "prompt": "Reference from input: [country]",
            "main": True,
            "output_type": "string",
            "name": "func2",
        },
    ],
}
var_dict = {"id": 1, "name": "country", "type": "input", "value": "china"}
function_dict = {
    "id": 2,
    "type": "standard",
    "prompt": "Reference from input: [country]",
    "main": True,
    "output_type": "string",
    "name": "func2",
}

with open(filename, "r") as file:
    data_dict = json.load(file)

program = pl.Program(data_dict)


# tests
# print(program._get_last_id_segment("1.1234.12345"))
# print(program._get_parent_id("1"))
# print(program.get_parent_program("1.1"))
# print(program.get_variable("1.ZJ1"))

# pl.run_function(function_dict, [var_dict])
# pl.run_program(program_dict)
# pl.run_program(program_dict)

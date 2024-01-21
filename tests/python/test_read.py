import sys
import os
import json
sys.path.append(os.getcwd() + r"\python")
import platogaze

program_1_path = "test_program_1.json"

test_program_1 = platogaze.load_from_json(file_path="test_program_1.json")

print(json.dumps(test_program_1.read("1"), indent=4))
print(json.dumps(test_program_1.read("2"), indent=4))
print(json.dumps(test_program_1.read("1.1"), indent=4))
print(json.dumps(test_program_1.read("1.2"), indent=4))

# {
#     "name": "test_program_2",
#     "variables": [
#         {
#             "id": 1,
#             "name": "country",
#             "type": "inputFieldValue",
#             "value": "china"
#         },
#         {
#             "id": 2,
#             "name": "google",
#             "type": "resourceURL",
#             "value": "www.google.com"
#         }
#     ],
#     "functions": [
#         {
#             "id": 1,
#             "type": "standard",
#             "main": true,
#             "prompt": "Reference from main [m0]",
#             "output_type": "string"
#         }
#     ]
# }


# {
#     "id": 2,
#     "type": "standard",
#     "prompt": "Reference from input: [i0]",
#     "main": true,
#     "output_type": "string"
# }


# test_program_1.get("3")["item"].display()
# test_program_1.get("1.1").display()
# test_program_1.get("2.1").display()
import sys
import os
sys.path.append(os.getcwd() + r"\python")
from platogaze import Program, Function
import platogaze

path_1 = "test_program_1.json"
program_1 = platogaze.load_from_json(file_path=path_1)
print("program_1:")
program_1.display()

print("Initialize the funtion")
function_1 = Function({
    "type": "standard",
    "prompt": "Hepe: [i0]",
    "main": True,
    "output_type": "string"
})
print("function_1:")
function_1.display()

# program_1:
# {
#     "name": "test_program_1",
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
#             "type": "program",
#             "program": {
#                 "name": "test_program_2",
#                 "variables": [
#                     {
#                         "id": 1,
#                         "name": "country",
#                         "type": "inputFieldValue",
#                         "value": "china"
#                     },
#                     {
#                         "id": 2,
#                         "name": "google",
#                         "type": "resourceURL",
#                         "value": "www.google.com"
#                     }
#                 ],
#                 "functions": [
#                     {
#                         "id": 1,
#                         "type": "standard",
#                         "main": true,
#                         "prompt": "Reference from main [m0]",
#                         "output_type": "string"
#                     }
#                 ]
#             }
#         },
#         {
#             "id": 2,
#             "type": "standard",
#             "prompt": "Reference from input: [i0]",
#             "main": true,
#             "output_type": "string"
#         }
#     ]
# }
# Initialize the funtion
# function_1:
# {
#     "type": "standard",
#     "prompt": "Hepe: [i0]",
#     "main": true,
#     "output_type": "string"
# }

# print('Update program["functions"][1] as function_1')
# program_1.update("function", function_1, "2")
# print("new program_1")
# program_1.display()

# new program_1
# {
#     "name": "test_program_1",
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
#             "type": "program",
#             "program": {
#                 "name": "test_program_2",
#                 "variables": [
#                     {
#                         "id": 1,
#                         "name": "country",
#                         "type": "inputFieldValue",
#                         "value": "china"
#                     },
#                     {
#                         "id": 2,
#                         "name": "google",
#                         "type": "resourceURL",
#                         "value": "www.google.com"
#                     }
#                 ],
#                 "functions": [
#                     {
#                         "id": 1,
#                         "type": "standard",
#                         "main": true,
#                         "prompt": "Reference from main [m0]",
#                         "output_type": "string"
#                     }
#                 ]
#             }
#         },
#         {
#             "id": 2,
#             "type": "standard",
#             "prompt": "Hepe: [i0]",
#             "main": true,
#             "output_type": "string"
#         }
#     ]
# }

print('Update program["functions"][0]["program"]["functions"][0] as function_1')
program_1.update("function", function_1, "1.1")
print("new program_1")
program_1.display()

# {
#     "name": "test_program_1",
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
#             "type": "program",
#             "program": {
#                 "name": "test_program_2",
#                 "variables": [
#                     {
#                         "id": 1,
#                         "name": "country",
#                         "type": "inputFieldValue",
#                         "value": "china"
#                     },
#                     {
#                         "id": 2,
#                         "name": "google",
#                         "type": "resourceURL",
#                         "value": "www.google.com"
#                     }
#                 ],
#                 "functions": [
#                     {
#                         "id": 1,
#                         "type": "standard",
#                         "prompt": "Hepe: [i0]",
#                         "main": true,
#                         "output_type": "string"
#                     }
#                 ]
#             }
#         },
#         {
#             "id": 2,
#             "type": "standard",
#             "prompt": "Reference from input: [i0]",
#             "main": true,
#             "output_type": "string"
#         }
#     ]
# }
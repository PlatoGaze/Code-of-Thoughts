import python.platogaze as pl
import json

# 假设 JSON 数据存储在 'data.json' 文件中
filename = "test_program_1.json"

with open(filename, "r") as file:
    data_dict = json.load(file)

program = pl.Program(data_dict)

# tests
# print(program._get_last_id_segment("1"))
# print(program._get_parent_id("1"))
# print(program.get_parent_program("1.1"))

#

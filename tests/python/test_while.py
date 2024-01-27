import sys
import os
import json
sys.path.append(os.getcwd() + r"\python")
import platogaze

while_program = platogaze.load_from_json("test_while.json")
while_program.display("while program:")

while_program.run()
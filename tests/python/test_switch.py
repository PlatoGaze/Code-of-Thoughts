import sys
import os
sys.path.append(os.getcwd() + r"\python")
import platogaze

switch_program = platogaze.load_from_json(file_path="switch_program.json")
switch_program.display("switch program:")

switch_program.run()
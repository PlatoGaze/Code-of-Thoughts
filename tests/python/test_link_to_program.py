import sys
import os
sys.path.append(os.getcwd() + r"\python")
import platogaze

test_run = platogaze.load_from_json(file_path="switch_program.json")
test_run.display("linked program:")

import sys
import os
sys.path.append(os.getcwd() + r"\python")
import platogaze

test_run = platogaze.load_from_json(file_path="test_run.json")
test_run.display()

test_run.run()
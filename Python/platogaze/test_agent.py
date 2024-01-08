from agent import Agent
from template import Template
from chain import Chain
import json

file_path = "Python/platogaze/my_template.json"
with open(file_path, "r") as f:
    data = json.load(f)
    
template = Template(data)
agent = Agent(template)
agent.execute()
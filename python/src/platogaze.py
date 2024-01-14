import json



def run(code):
    # Your traversal logic goes here
    print(f"ID: {code['id']}, Type: {code['type']}")

    # Recursive traversal for child expressions or functions
    for expression_of_code in code.get("expressions", []):
        run(expression_of_code)


file_path = "python/tests/code.json"

# Load JSON data from file
with open(file_path, 'r') as file:
    data = json.load(file)

# Traverse the function starting from the root
run(data)

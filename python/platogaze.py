import json


class Function:
    def __init__(self, function_dict: dict) -> None:
        if self.is_valid(function_dict):
            self.properties = function_dict
        else:
            raise ValueError("Invalid funtion format")

    def is_valid(self, function_dict):
        return True

    def to_dict(self):
        return self.properties.copy()

    def display(self):
        print(json.dumps(self.to_dict(), indent=4))


class Program:
    def __init__(self, program_dict: dict) -> None:
        """
        Initializes an instance of MyClass with a program dictionary.

        Args:
            program_dict (dict): A dictionary representing the program.

        Raises:
            ValueError: If the program format is invalid.
        """
        if self.is_valid(program_dict):
            self.properties = program_dict
        else:
            raise ValueError("Invalid program format")

    def is_valid(self, program_dict: dict):
        return True

    def to_dict(self):
        """
        Converts the program object to a dictionary.

        Returns:
            dict: A dictionary representation of the program object.
        """
        return self.properties.copy()

    def display(self):
        print(json.dumps(self.to_dict(), indent=4))

    def get_parent_program(self, id: str = ""):
        references = id.split('.')
        program = self.properties
        if id != "":
            for ix in range(0, len(references) - 1):
                refer = references[ix]
                program = program["functions"][int(refer) - 1]["program"]
        return program
    
    def get_program(self, id: str = "1"):
        references = id.split('.')
        program = self.properties
        if id != "":
            for ix in range(0, len(references)):
                refer = references[ix]
                program = program["functions"][int(refer) - 1]["program"]
        return program

    def get(self, id: str = ""):
        program = self.get_parent_program(id)
        references = id.split('.')
        program = program["functions"][int(references[-1]) - 1]
        if "program" in program:
            return {
                "type": "program",
                "item": Program(program["program"])
            }
        else:
            return {
                "type": "function",
                "item": Function(program)
            }

    def add_program(self, new_program, id: str = ""):
        references = id.split('.')
        program = self.get_program(id)
        if isinstance(new_program, Program):
            new_program = new_program.to_dict()
        elif isinstance(new_program, dict):
            new_program = Program(new_program)
            new_program = new_program.to_dict()
        else:
            raise TypeError("Invalid type: " + type(new_program) +
                            ", should be a Program or dict")
        new_id = len(program["functions"]) + 1
        program["functions"].append({
            "id": new_id,
            "type": "program",
            "program": new_program
        })

    def add_function(self, new_function, id: str):
        references = id.split('.')
        program = self.get_program(id)
        if isinstance(new_function, Function):
            new_function = new_function.to_dict()
        elif isinstance(new_function, dict):
            new_function = Function(new_function)
            new_function = new_function.to_dict()
        else:
            raise TypeError("Invalid type: " + type(new_function) +
                            ", should be a Funtion or dict")
        new_id = len(program["functions"]) + 1
        program["functions"].append({
            "id": new_id,
            **new_function
        })

    def add_variable(self, item: dict, id: str = "i"):
        """
        Adds a variable to the specified parent program.

        Args:
            item (dict): The variable item to be added.
            id (str): The ID of the parent program.

        Raises:
            TypeError: If item is not a dictionary.

        Returns:
            None
        """
        # Check if item is a dictionary
        if not isinstance(item, dict):
            raise TypeError(
                f"Variable item should be a dictionary, instead it is {type(item)}.")

        # Extract the type from the first character of id
        var_type = id[0]

        # Determine the type based on the first character of id
        if var_type == 'i':
            item['type'] = 'inputFieldValue'
        elif var_type == 'u':
            item['type'] = 'resourceURL'
        else:
            raise ValueError(f"Invalid variable type: {var_type}")
        
        # Exclude the first character from id when getting the parent program
        program = self.get_program(id[1:])
        
        item['id'] = len(program["variables"]) + 1

        # Append the variable item to program["variables"]
        program["variables"].append(item)

    def add(self, type: str, item, id: str = ""):
        if type == "program":
            self.add_program(item, id)
        elif type == "function":
            self.add_function(item, id)
        elif type == "variable":
            self.add_variable(item, id)
        else:
            raise TypeError("Unrecognized type: " + type)


def create(name="undefined", **kwargs) -> Program:
    program_dict = {
        "name": name,
        "variables": kwargs.get("variables", [])
    }
    program = Program(program_dict)
    return program


def load_from_json(file_path: str) -> Program:
    with open(file_path, "r") as file:
        data = json.load(file)
    return Program(data)

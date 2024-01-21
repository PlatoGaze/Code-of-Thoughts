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
        Initializes an instance of Program with a program dictionary.

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

    def get_program(self, id: str = "1"):
        """
        Retrieves the program based on the given ID.

        Args:
            `id` (str): The ID of the program to retrieve. Defaults to "1".

        Returns:
            `dict`: The program corresponding to the given ID.
        """
        references = id.split('.')
        if id == "":
            return self.properties
        
        program = self.properties
        for ix in range(0, len(references)):
            refer = references[ix]
            program = program["functions"][int(refer) - 1]["program"]
        return program

    def get_parent_program(self, id: str):
        """
        Retrieves the parent program of the given ID.

        Args:
            `id` (str): The ID of the program.

        Returns:
            The parent program object.
            
            update function 1.2
        """
        references = id.split(".")
        return self.get_program(".".join(references[:-1]))
    
    def get_variable(self, id: str) -> dict:
        references = id.split('.')
        program = self.get_program(".".join(references[:-1]))
        variable = program["variables"][int(references[-1]) - 1]
        return variable

    def get(self, id: str = "") -> dict:
            """
            Retrieves a program or function based on the given ID.

            Args:
                id (str): The ID of the program or function to retrieve.

            Returns:
                str or dict: The program or function corresponding to the given ID.
            """
            if id == "":  # return the root program
                return self.properties
            # if the first char of id is an alphabet, then we should call get_variable
            if id[0].isalpha():
                return self.get_variable(id[1:])
            references = id.split('.')
            program = self.get_program(".".join(references[:-1]))
            program = program["functions"][int(references[-1]) - 1]
            if "program" in program:
                return program["program"]
            else:
                return program


    def add_program(self, new_program, id: str = ""):
        """
        Adds a new program to the existing program list.

        Args:
            `new_program` (``Program`` or `dict`): The new program to be added. It can be either a `Program` object or a dictionary.
            id (str, optional): The ID of the program whose functions will be appended. Consider the id as the folder's path. If not provided, a new program will be added to the root path.

        Raises:
            `TypeError`: If the new_program is not of type `Program` or dict.

        Returns:
            `None`
        """
        program = self.get(id)
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
        """
        Adds a new function to the program identified by the given ID.

        Args:
            `new_function` (Function or dict): The new function to be added. It can be either a Function object or a dictionary representing the function.
            id (str): The ID of the program where the function should be added.

        Raises:
            TypeError: If the new_function parameter is not of type Function or dict.

        Returns:
            None
        """
        program = self.get(id)
        if isinstance(new_function, Function):
            new_function = new_function.to_dict()
        elif isinstance(new_function, dict):
            new_function = Function(new_function)
            new_function = new_function.to_dict()
        else:
            raise TypeError("Invalid type: " + type(new_function) +
                            ", should be a Function or dict")
        new_id = len(program["functions"]) + 1
        program["functions"].append({
            "id": new_id,
            **new_function
        })

    def add_variable(self, item: dict, id: str):
        """
        Adds a variable to the program.

        Args:
            item (dict): The variable item to be added. Should be a dictionary.
            id (str): The ID of the program.

        Raises:
            TypeError: If the item is not a dictionary.
            ValueError: If the variable type is invalid.

        Returns:
            None
        """
        if not isinstance(item, dict):
            raise TypeError(
                f"Variable item should be a dictionary, instead it is {type(item)}.")

        var_type = id[0]

        if var_type == 'i':
            item['type'] = 'inputFieldValue'
        elif var_type == 'u':
            item['type'] = 'resourceURL'
        else:
            raise ValueError(f"Invalid variable type: {var_type}")

        program = self.get(id[1:])
        item['id'] = len(program["variables"]) + 1

        program["variables"].append(item)

    def add(self, type: str, item, id: str = ""):
        """
        Adds an item of the specified type to the PlatoGaze object.

        Parameters:
        - type (str): The type of item to add. Valid values are "program", "function", and "variable".
        - item: The item to add.
        - id (str): Optional. The ID of the item.

        Raises:
        - TypeError: If the specified type is not recognized.

        Returns:
        None
        """
        if type == "program":
            self.add_program(item, id)
        elif type == "function":
            self.add_function(item, id)
        elif type == "variable":
            self.add_variable(item, id)
        else:
            raise TypeError("Unrecognized type: " + type)

    def update_program(self, new_program, id: str = ""):
        """
        Updates the program at the specified ID with the new program.

        Args:
            new_program (Program or dict): The new program to update with.
            id (str): The ID of the program to update. Defaults to an empty string.

        Raises:
            TypeError: If the new_program is not of type Program or dict.

        Returns:
            None
        """
        if isinstance(new_program, Program):
            new_program = new_program.to_dict()
        elif isinstance(new_program, dict):
            new_program = Program(new_program)
            new_program = new_program.to_dict()
        else:
            raise TypeError("Invalid type: " + type(new_program) +
                            ", should be a Program or dict")
        original = self.get(id)
        original.update(new_program)

    def update_function(self, new_function, id: str):
        """
        Update a function in the program with the given ID.

        Args:
            new_function (Union[Function, dict]): The new function to update. It can be either a Function object or a dictionary.
            id (str): The ID of the function to update.

        Raises:
            TypeError: If the new_function is not of type Function or dict.

        Returns:
            None
        """
        program = self.get(id)
        if isinstance(new_function, Function):
            new_function = new_function.to_dict()
        elif isinstance(new_function, dict):
            new_function = Function(new_function)
            new_function = new_function.to_dict()
        else:
            raise TypeError("Invalid type: " + type(new_function) +
                            ", should be a Function or dict")
        program.update(new_function)

    def update_variable(self, item: dict, id: str = "i1"):
        if not isinstance(item, dict):
            raise TypeError(
                f"Variable item should be a dictionary, instead it is {type(item)}.")

        var_type = id[0]

        if var_type == 'i':
            item['type'] = 'inputFieldValue'
        elif var_type == 'u':
            item['type'] = 'resourceURL'
        else:
            raise ValueError(f"Invalid variable type: {var_type}")

        references = id[1:].split(".")
        program = self.get(".".join(references[:-1]))
        ix = int(references[-1]) - 1
        program["variables"][ix].update(item)

    def update(self, type: str, item, id: str = ""):
        """
        Update the specified item based on the given type.

        Parameters:
        - type (str): The type of item to update. Valid values are "program", "function", or "variable".
        - item: The item to update.
        - id (str): The ID of the item (optional).

        Raises:
        - TypeError: If the type is unrecognized.

        Returns:
        - None
        """
        if type == "program":
            self.update_program(item, id)
        elif type == "function":
            self.update_function(item, id)
        elif type == "variable":
            self.update_variable(item, id)
        else:
            raise TypeError("Unrecognized type: " + type)


def create_program(name: str = "undefined"):
    return Program({
        "name": name,
        "variables": [],
        "functions": []
    })


def create_function(function_dict: dict):
    return Function({
        "type": function_dict.get("type", "standard"),
        "main": function_dict.get("main", True),
        "prompt": function_dict.get("prompt", ""),
        "output_type": function_dict.get("output_type", "string")
    })


def create_variable(variable_dict: dict):
    return {
        "type": variable_dict.get("type", "inputFieldValue"),
        "name": variable_dict.get("name", "undefined"),
        "value": variable_dict.get("value", "")
    }


def create(type: str = "program", value: dict = {}):
    if type == "program":
        return create_program(value.get("name", "undefined"))
    elif type == "function":
        return create_function(value)
    elif type == "variable":
        return create_variable(value)
    else:
        raise TypeError("Unrecognized type: " + type)


def load_from_json(file_path: str) -> Program:
    with open(file_path, "r") as file:
        data = json.load(file)
    return Program(data)

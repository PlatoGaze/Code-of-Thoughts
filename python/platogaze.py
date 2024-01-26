import json
import os
import copy


class Function:
    def __init__(self, function_dict: dict) -> None:
        if Function.is_valid(function_dict):
            self.properties = function_dict
        else:
            raise ValueError("Invalid function format")

    @staticmethod
    def is_valid(function_dict):
        # check whether the function dict contain keys: name, type, prompt, output_type
        if function_dict['type'] == 'standard':
            check_keys = ["name", "prompt", "output_type"]
            for key in check_keys:
                if key not in function_dict:
                    raise ValueError(
                        f"Invalid function format: missing key: {key}\nfunction: {function_dict}")
        elif function_dict['type'] == 'switch':
            check_keys = ["name", "output_type", "cases"]
            for key in check_keys:
                if key not in function_dict:
                    raise ValueError(
                        f"Invalid function format: missing key: {key}\nfunction name: {function_dict['name']}")
            for case in function_dict['cases']:
                check_keys = ['value', 'program']
                for key in check_keys:
                    if key not in case:
                        raise ValueError(
                            f"Invalid function format: missing key: {key}\nfunction_name: {function_dict['name']}")

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
        program_dict = copy.deepcopy(program_dict)
        if Program.is_valid(program_dict):
            self.properties = program_dict
        else:
            raise ValueError("Invalid program format")

        self.add_type_methods = {
            "program": self.add_program,
            "function": self.add_function,
            "variable": self.add_variable
        }

        self.update_type_methods = {
            "program": self.update_program,
            "function": self.update_function,
            "variable": self.update_variable
        }

        self.save_to_file()
        print("Program: " + self.properties['name'] + " saved to file.")

    @staticmethod
    def is_valid(program_dict: dict):
        check_keys = ["name", "variables", "functions"]
        for key in check_keys:
            if key not in program_dict:
                raise ValueError("Invalid program format: missing key: " +
                                 key + "\nprogram name: " + program_dict['name'])

        variable_keys = ["type", "name", "value"]
        variable_types = ["input", "url", "fixed", "note", "function_output"]
        for variable in program_dict.get("variables", []):
            for key in variable_keys:
                if key not in variable:
                    raise ValueError(
                        "Invalid variable format: missing key:" + key + "\nprogram name: " + program_dict['name'])
            if variable["type"] not in variable_types:
                raise ValueError(
                    "Invalid variable type: " + variable['type'] + "\nprogram name:" + program_dict['name'])

        for function in program_dict.get("functions", []):
            if function.get("type") == "program":
                if not Program.is_valid(function["program"]):
                    return False
            else:
                if not Function(function).is_valid(function):
                    return False

        return True

    def save_to_file(self):
        try:
            program_name = self.properties["name"]
        except KeyError:
            print("Error: 'name' key not found in properties.")
            return

        directory = "download"
        # Create a folder named after the program name inside the 'download' folder
        program_folder = os.path.join(directory, program_name)
        os.makedirs(program_folder, exist_ok=True)

        # Create and save main.json inside the program folder
        main_json_path = os.path.join(program_folder, "main.json")
        main_data = {
            "name": program_name,
            "variables": self.properties.get("variables", []),
            "functions": []
        }

        # Traverse self.properties["functions"]
        for function_data in self.properties.get("functions", []):
            if function_data.get("type") == "program":
                # If it's a program type, create a link
                program_data = {
                    "id": function_data["id"], "program": function_data["program"]["name"]}
                main_data["functions"].append(program_data)

                # Save the program data in a separate file
                program_json_path = os.path.join(
                    program_folder, function_data["program"]["name"] + ".json")
                with open(program_json_path, "w") as program_file:
                    json.dump(function_data["program"], program_file, indent=4)
            else:
                # If it's a function type, add it to main.json's functions
                main_data["functions"].append(function_data)

        # Save main.json inside the program folder
        with open(main_json_path, "w") as main_file:
            json.dump(main_data, main_file, indent=4)

        print(f"Files saved successfully for program: {program_name}")

    def download_on_change(method):
        """This method is a decorator for all methods that change the program object. It will automatically save the program to a file after the method is executed.

        Args:
            method (function): The method to be decorated.
        """

        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            # check validity when properties are changed
            Program.is_valid(self.properties)
            self.save_to_file()
            print("Program saved to file.")
            return result
        return wrapper

    def to_dict(self):
        """
        Converts the program object to a dictionary.

        Returns:
            dict: A dictionary representation of the program object.
        """
        return self.properties.copy()

    def display(self, msg=""):
        print(msg)
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

    def read(self, id: str = "") -> dict:
        """
        Retrieves a program or function based on the given ID.

        Args:
            id (str): The ID of the program or function to retrieve.
            If try to read a variable, the id should be like "v1" (any variable type + variable id)

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
        program = self.read(id)
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
        program = self.read(id)
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
            item['type'] = 'input'
        elif var_type == 'u':
            item['type'] = 'url'
        else:
            raise ValueError(f"Invalid variable type: {var_type}")

        program = self.read(id[1:])
        item['id'] = len(program["variables"]) + 1

        program["variables"].append(item)

    @download_on_change
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
        item = copy.deepcopy(item)
        add_func = self.add_type_methods.get(type)
        if add_func:
            add_func(item, id)
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
        original = self.read(id)
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
        program = self.read(id)
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
            item['type'] = 'input'
        elif var_type == 'u':
            item['type'] = 'url'
        else:
            raise ValueError(f"Invalid variable type: {var_type}")

        references = id[1:].split(".")
        program = self.read(".".join(references[:-1]))
        ix = int(references[-1]) - 1
        program["variables"][ix].update(item)

    @download_on_change
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
        item = copy.deepcopy(item)
        update_func = self.update_type_methods.get(type)
        if update_func:
            update_func(item, id)
        else:
            raise TypeError("Unrecognized type: " + type)

    @staticmethod
    def replace_variables(prompt: str, variables: list):
        for variable in variables:
            prompt = prompt.replace(f"[{variable['name']}]", variable['value'])
        # if there is still [] quoted part in the prompt, warn the user about possibly incorrect reference
        if "[" in prompt or "]" in prompt:
            print("Warning: there might be incorrect reference in the prompt: " + prompt)
        return prompt

    def run_function(self, function_dict: dict, variables):
        # in the prompt of a function, reference to variables are quoted in [], so before calling the language model, we need to replace the reference with the actual value
        # for example, if the prompt is "Hello [name]", and the value of name is "John", then the prompt should be "Hello John"
        prompt = Program.replace_variables(function_dict["prompt"], variables)
        if (function_dict["type"] == "standard"):
            answer = fake_api_call(prompt)
            print("----------------------------------------------")
            print("Function: " + function_dict['name'] +
                  "\nPrompt: " + prompt + "\nAnswer: " + answer)
            print("----------------------------------------------")
            function_dict["answer"] = answer
        elif (function_dict["type"] == "switch"):
            pass
        else:
            print("Error: unrecognized function type: " +
                  function_dict["type"])

    def run_program(self, program_dict: dict):
        for function_or_program in program_dict["functions"]:
            if function_or_program["type"] == "program":
                self.run_program(function_or_program["program"])
            else:
                self.run_function(function_or_program,
                                  program_dict["variables"])

    def run(self):
        """
        Runs the program.

        Returns:
            None
        """
        program_dict = self.properties
        for function_or_program in program_dict["functions"]:
            if function_or_program["type"] == "program":
                self.run_program(function_or_program["program"])
            else:
                self.run_function(function_or_program,
                                  program_dict["variables"])


def create_program(*args, **kwargs):
    return Program({
        "name": kwargs.get("name", "undefined"),
        "variables": [],
        "functions": []
    })


def create_function(*args, **kwargs):
    return Function({
        "name": kwargs.get("name", "undefined"),
        "type": kwargs.get("type", "standard"),
        "main": kwargs.get("main", True),
        "prompt": kwargs.get("prompt", ""),
        "output_type": kwargs.get("output_type", "string")
    })


def create_variable(*args, **kwargs):
    return {
        "type": kwargs.get("type", "input"),
        "name": kwargs.get("name", "undefined"),
        "value": kwargs.get("value", "")
    }


create_type_methods = {
    "program": create_program,
    "function": create_function,
    "variable": create_variable
}


def create(type: str = "program", *args, **kwargs):
    """
    Creates a new item of the specified type.

    Args:
        type (str): The type of item to create. Valid values are "program", "function", and "variable".
        value (dict): The initial values of the item.

    Raises:
        TypeError: If the type is unrecognized.

    Returns:
        The newly created item.
    """
    create_func = create_type_methods.get(type)
    if create_func:
        return create_func(**kwargs)
    else:
        raise TypeError("Unrecognized type: " + type)


def link_to_program(program_dict: dict):
    # traverse the functions in program_dict, if the function is program, go recursive; if not, if we encounter a key named 'program' and the corresponding value is a str instead of a dict, then we should link it to the corresponding program. The linked program should be found in local folder with the same name.json
    for function in program_dict["functions"]:
        if function["type"] == "program":
            link_to_program(function["program"])
        elif function['type'] == 'switch':
            for item in function['cases']:
                if isinstance(item['program'], str) and item['program'] != '':
                    file_path = item['program'] + '.json'
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                    item['program'] = data
                    link_to_program(item['program'])
                elif item['program'] == "":
                    empty_program = create_program(name="empty").to_dict()
                    item['program'] = empty_program
    return program_dict


def load_from_json(file_path: str) -> Program:
    """
    Load data from a JSON file and return a Program object.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Program: The Program object created from the JSON data.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    link_to_program(data)
    return Program(data)


def fake_api_call(prompt: str):
    return "This is a fake api call."

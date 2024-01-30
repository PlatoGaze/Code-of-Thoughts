import json
import os
import copy
import re


class Variable:
    #!这儿初始化要可以输入参数而不是dict
    def __init__(self, variable_dict: dict) -> None:
        try:
            self.variable_dict = Variable.validate_and_initialize(variable_dict)
        except ValueError:
            raise ValueError("Invalid function format")

    @staticmethod
    def validate_and_initialize(variable_dict: dict):
        try:
            if variable_dict["type"] in [
                "standard",
                "web",
                "fixed",
                "function_output",
            ]:
                required_keys = ["name", "type", "value"]
                # Check if all required keys are in the dictionary
                if all(key in variable_dict for key in required_keys):
                    return {
                        "name": variable_dict["name"],
                        "type": variable_dict["type"],
                        "value": variable_dict["value"],
                    }
                else:
                    raise ValueError("Missing one or more required keys.")
            else:
                raise ValueError("Invalid Variable type.")
        except Exception as e:
            raise ValueError(f"Invalid variable format: {e}")


class Function:
    #! 这儿初始化要可以输入参数而不是dict
    def __init__(self, function_dict: dict) -> None:
        try:
            Function.is_valid(function_dict)
            self.function_dict = function_dict
        except ValueError:
            raise ValueError("Invalid function format")

    @staticmethod
    def is_valid(function_dict):
        if function_dict["type"] == "standard":
            check_keys = ["name", "prompt", "output_type"]
            if not all(key in function_dict for key in check_keys):
                missing_keys = [key for key in check_keys if key not in function_dict]
                raise ValueError(
                    f"Invalid function format: missing keys: {missing_keys}\nfunction: {function_dict}"
                )
        elif function_dict["type"] == "switch":
            check_keys = ["name", "output_type", "cases"]
            if not all(key in function_dict for key in check_keys):
                missing_keys = [key for key in check_keys if key not in function_dict]
                raise ValueError(
                    f"Invalid function format: missing keys: {missing_keys}\nfunction name: {function_dict['name']}"
                )
            for case in function_dict["cases"]:
                check_keys = ["value", "program"]
                if not all(key in case for key in check_keys):
                    missing_keys = [key for key in check_keys if key not in case]
                    raise ValueError(
                        f"Invalid function format: missing keys: {missing_keys}\nfunction_name: {function_dict['name']}"
                    )

        return True

    def to_dict(self):
        return self.function_dict.copy()

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
        self.program_dict = copy.deepcopy(program_dict)
        if not Program.is_valid(self.program_dict):
            raise ValueError("Invalid program format")

        self.add_type_methods = {
            "program": self.add_program,
            "function": self.add_function,
            "variable": self.add_variable,
        }

        self.update_type_methods = {
            "program": self.update_program,
            "function": self.update_function,
            "variable": self.update_variable,
        }

    @staticmethod
    def is_valid(program_dict: dict):
        """
        Checks if the given program dictionary is valid.

        Args:
            program_dict (dict): The program dictionary to validate.

        Raises:
            ValueError: If the program dictionary is missing any required keys or has invalid variable types.

        Returns:
            bool: True if the program dictionary is valid, False otherwise.
        """
        check_keys = ["name", "variables", "functions"]
        for key in check_keys:
            if key not in program_dict:
                raise ValueError(
                    "Invalid program format: missing key: "
                    + key
                    + "\nprogram name: "
                    + program_dict["name"]
                )

        variable_keys = ["type", "name", "value"]
        variable_types = ["input", "url", "fixed", "note", "function_output"]
        for variable in program_dict.get("variables", []):
            for key in variable_keys:
                if key not in variable:
                    raise ValueError(
                        "Invalid variable format: missing key:"
                        + key
                        + "\nprogram name: "
                        + program_dict["name"]
                    )
            if variable["type"] not in variable_types:
                raise ValueError(
                    "Invalid variable type: "
                    + variable["type"]
                    + "\nprogram name:"
                    + program_dict["name"]
                )

        for function in program_dict.get("functions", []):
            if function.get("type") == "program":
                if not Program.is_valid(function["program"]):
                    return False
            else:
                if not Function(function).is_valid(function):
                    return False

        return True

    def save(self):
        """
        Saves the program data to files.

        This method creates a folder named after the program name inside the 'download' folder.
        It then saves the program data in JSON format to separate files, including main.json and any linked program files.

        Raises:
            KeyError: If the 'name' key is not found in the properties dictionary.

        Returns:
            None
        """
        try:
            program_name = self.program_dict["name"]
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
            "variables": self.program_dict.get("variables", []),
            "functions": [],
        }

        # Traverse self.program_dict["functions"]
        for function_data in self.program_dict.get("functions", []):
            if function_data.get("type") == "program":
                # If it's a program type, create a link
                program_data = {
                    "id": function_data["id"],
                    "program": function_data["program"]["name"],
                }
                main_data["functions"].append(program_data)

                # Save the program data in a separate file
                program_json_path = os.path.join(
                    program_folder, function_data["program"]["name"] + ".json"
                )
                with open(program_json_path, "w") as program_file:
                    json.dump(function_data["program"], program_file, indent=4)
            else:
                # If it's a function type, add it to main.json's functions
                main_data["functions"].append(function_data)

        # Save main.json inside the program folder
        with open(main_json_path, "w") as main_file:
            json.dump(main_data, main_file, indent=4)

        print(f"Files saved successfully for program: {program_name}")

    def download(method):
        """This method is a decorator for all methods that change the program object. It will automatically save the program to a file after the method is executed.

        Args:
            method (function): The method to be decorated.
        """

        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            # check validity when properties are changed
            Program.is_valid(self.program_dict)
            self.save()
            print("Program saved to file.")
            return result

        return wrapper

    def to_dict(self):
        return self.program_dict.copy()

    def display(self, msg=""):
        print(msg)
        print(json.dumps(self.to_dict(), indent=4))

    def get_program(self, id: str = "1"):
        references = id.split(".")

        program = self.program_dict
        for ix in range(0, len(references)):
            refer = references[ix]
            program = program["functions"][int(refer) - 1]["program"]
        return program

    def get_parent_program(self, id: str):
        parent_id = self._get_parent_id(id)
        return self.get_program(parent_id)

    def get_variable(self, id: str) -> dict:
        program = self.get_parent_program(id)
        # print(self._get_last_id_segment(id))
        variable = program["variables"][int(self._get_last_id_segment(id))]
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
            return self.program_dict
        # if the first char of id is an alphabet, then we should call get_variable
        if id[0].isalpha():
            return self.get_variable(id[1:])
        references = id.split(".")
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
            raise TypeError(
                "Invalid type: " + type(new_program) + ", should be a Program or dict"
            )
        new_id = len(program["functions"]) + 1
        program["functions"].append(
            {"id": new_id, "type": "program", "program": new_program}
        )

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
            raise TypeError(
                "Invalid type: " + type(new_function) + ", should be a Function or dict"
            )
        new_id = len(program["functions"]) + 1
        program["functions"].append({"id": new_id, **new_function})

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
                f"Variable item should be a dictionary, instead it is {type(item)}."
            )

        var_type = id[0]

        if var_type == "i":
            item["type"] = "input"
        elif var_type == "u":
            item["type"] = "url"
        else:
            raise ValueError(f"Invalid variable type: {var_type}")

        program = self.read(id[1:])
        item["id"] = len(program["variables"]) + 1

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
        item = copy.deepcopy(item)
        try:
            self.add_type_methods[type](item, id)
        except KeyError:
            raise TypeError(f"Unrecognized type: {type}")

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
            raise TypeError(
                "Invalid type: " + type(new_program) + ", should be a Program or dict"
            )
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
            raise TypeError(
                "Invalid type: " + type(new_function) + ", should be a Function or dict"
            )
        program.update(new_function)

    def update_variable(self, item: dict, id: str = "i1"):
        """
        Updates a variable in the program based on the given item and ID.

        Args:
            item (dict): The dictionary containing the updated variable information.
            id (str, optional): The ID of the variable to be updated. Defaults to "i1".

        Raises:
            TypeError: If the item is not a dictionary.
            ValueError: If the variable type is invalid.

        Returns:
            None
        """
        if not isinstance(item, dict):
            raise TypeError(
                f"Variable item should be a dictionary, instead it is {type(item)}."
            )

        var_type = id[0]

        if var_type == "i":
            item["type"] = "input"
        elif var_type == "u":
            item["type"] = "url"
        else:
            raise ValueError(f"Invalid variable type: {var_type}")

        references = id[1:].split(".")
        program = self.read(".".join(references[:-1]))
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
        item = copy.deepcopy(item)
        try:
            self.update_type_methods[type](item, id)
        except KeyError:
            raise TypeError(f"Unrecognized type: {type}")

    def run(self):
        """
        Runs the program.
        """
        for function in self.program_dict["functions"]:
            if function["type"] == "program":
                run_program(function["program"])
            else:
                run_function(function, self.program_dict["variables"])

    def _get_parent_id(self, id: str):
        self._is_valid_id(id)
        last_dot_index = id.rfind(".")
        if last_dot_index == -1:
            raise ValueError("Invalid ID: Child ID must contain a '.' character")

        parent_id = id[:last_dot_index]
        return parent_id

    def _get_last_id_segment(self, id: str):
        self._is_valid_id(id)
        return id.split(".")[-1]

    def _is_valid_id(self, id: str):
        _check_is_string(id)  # 假设这是一个检查 id 是否为字符串的函数
        pattern = r"^\d+\.\d+\.\d+$"
        if not re.match(pattern, id):
            raise ValueError(f"Invalid ID format: {id}")


#! 把初始化也得加入
#! 不要飘在外面，把create_program 放到 Program 里，或直接删了
def create_program(*args, **kwargs):
    # 读取 'name'，为其他字段提供默认值
    program_dict = {
        "name": kwargs["name"],
        "variables": kwargs.get("variables", []),
        "functions": kwargs.get("functions", []),
    }

    return Program(program_dict)


#! 不要飘在外面，把create_function放到 Function 里，或直接删了
def create_function(*args, **kwargs):
    arg_names = ["name", "type", "main", "prompt", "output_type"]
    defaults = {
        "name": "undefined",
        "type": "standard",
        "main": True,
        "prompt": "",
        "output_type": "string",
    }

    # 使用 args 填充参数
    params = dict(zip(arg_names, args))

    # 使用 kwargs 填充或覆盖参数
    params.update(kwargs)

    # 确保所有参数都有值，使用默认值填充缺失的参数
    for key in arg_names:
        params.setdefault(key, defaults[key])

    return Function(params)


#! 需要给variable一个新的类
#! 定义方式很怪.表现在不能按顺序读入，只能kwargs读入
#! 更怪的地方是，它应该出现在 Variable 类里
def create_variable(*args, **kwargs):
    variable_dict = kwargs
    try:
        variable_type = variable_dict["type"]
        if variable_type in ["standard", "web", "fixed", "function_output"]:
            return Variable(
                {
                    "name": variable_dict["name"],
                    "type": variable_type,
                    "value": variable_dict["value"],
                }
            )
    except SyntaxError as e:
        print(f"Error: {e}")
        return None


# function, variable, program是组成整个项目的基本类型，它们各自的变量统称为object.
# object_factory_registry 是目录，保存了创建各个基本类型的变量的创建方式
_object_factory_registry = {
    "program": create_program,
    "function": create_function,
    "variable": create_variable,
}


def create(type: str = "program", *args, **kwargs):
    try:
        create_func = _object_factory_registry.get(type)
        return create_func(**kwargs)
    except TypeError:
        raise TypeError("Unrecognized type: " + type)


#! 应该在 run 里面 recursively 去查，返回给我的应该是 result


#!  update variable type 为 function_output 的东西。返回所以 type main的函数的output
def run_program(program_dict: dict):
    """
    Recursively runs the program specified in the program_dict.

    Args:
        program_dict (dict): A dictionary containing the program to be executed.

    Returns:
        None
    """
    print(program_dict)
    for function in program_dict["functions"]:
        if function["type"] == "program":
            run_program(function["program"])
        else:
            run_function(function, program_dict["variables"])


#!  update variable type 为 function_output 的东西
def run_function(function_dict: dict, variables):
    """
    Runs a function based on the provided function dictionary and variables.

    Args:
        function_dict (dict): A dictionary containing information about the function.
        variables: The variables to be used in the function.

    Returns:
        None
    """
    # in the prompt of a function, reference to variables are quoted in [], so before calling the language model, we need to replace the reference with the actual value
    # for example, if the prompt is "Hello [name]", and the value of name is "John", then the prompt should be "Hello John"

    if function_dict["type"] == "standard":
        prompt = _fill_in_variables_in_prompt(function_dict["prompt"], variables)
        answer = api_call(prompt)
        print("----------------------------------------------")
        print(
            "Function: "
            + function_dict["name"]
            + "\nPrompt: "
            + prompt
            + "\nAnswer: "
            + answer
        )
        print("----------------------------------------------")
        function_dict["answer"] = answer

    elif function_dict["type"] == "switch":
        condition_name = function_dict["condition"]
        # traverse the variables list, find a variable whose name is condition_name
        for variable in variables:
            if variable["name"] == condition_name:
                condition_value = variable["value"]
                break
        # traverse the cases list, find the case whose value is equal to condition_value

        run_default = True
        for case in function_dict["cases"]:
            if case["value"] == condition_value:
                run_default = False
                case_program = case["program"]
            if case["value"] == "default":
                default_program = case["program"]
        # run the program in the case
        if run_default:
            case_program = default_program

        if "type" not in case_program:
            run_program(case_program)
        else:
            run_function(case_program, variables)

    elif function_dict["type"] == "while":
        variable_l = None
        for variable in variables:
            if variable["name"] == function_dict["condition_l"]:
                variable_l = variable
                break
        if variable_l is None:
            raise ValueError(
                "Error: condition_l ["
                + function_dict["condition_l"]
                + "] is not found in variables list"
            )
        variable_r = None
        for variable in variables:
            if variable["name"] == function_dict["condition_r"]:
                variable_r = variable
                break
        if variable_r is None:
            raise ValueError(
                "Error: condition_r ["
                + function_dict["condition_r"]
                + "] is not found in variables list"
            )

        while variable_l["value"] != variable_r["value"]:
            # assume body is a list of function
            for function in function_dict["body"]:
                run_function(function, variables)
    else:
        print("Error: unrecognized function type: " + function_dict["type"])
        return

    if "return" in function_dict and function_dict["return"] != "":
        # change the corresponding variable's value
        for variable in variables:
            if variable["name"] == function_dict["return"]:
                variable["value"] = function_dict["answer"]
                break


def _fill_in_variables_in_prompt(prompt: str, variables: list):
    """
    Replaces variables in the given prompt with their corresponding values.

    Args:
        prompt (str): The prompt string containing variables to be replaced.
        variables (list): A list of dictionaries, where each dictionary contains the name and value of a variable.

    Returns:
        str: The prompt string with variables replaced by their values.
    """
    for variable in variables:
        prompt = prompt.replace(f"[{variable['name']}]", variable["value"])
    # if there is still [] quoted part in the prompt, warn the user about possibly incorrect reference
    if "[" in prompt or "]" in prompt:
        print("Warning: there might be incorrect reference in the prompt: " + prompt)
    return prompt


def api_call(prompt: str):
    return input(
        prompt + '\ninput your answer here (default is "This is a fake api call"): '
    )


def _check_is_string(input):
    if not isinstance(input, str):
        raise TypeError("Expected a string")

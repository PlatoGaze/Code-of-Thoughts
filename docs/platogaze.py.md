<!-- markdownlint-disable -->

<a href="..\python\platogaze.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `platogaze.py`




**Global Variables**
---------------
- **create_type_methods**

---

<a href="..\python\platogaze.py#L614"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_program`

```python
create_program(*args, **kwargs)
```

Create a new program object. 



**Args:**
 
 - <b>`*args`</b>:  Variable length argument list. 
 - <b>`**kwargs`</b>:  Arbitrary keyword arguments. 



**Returns:**
 
 - <b>`Program`</b>:  The newly created program object. 


---

<a href="..\python\platogaze.py#L632"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_function`

```python
create_function(*args, **kwargs)
```

Create a new function object. 



**Args:**
 
 - <b>`*args`</b>:  Variable length arguments. 
 - <b>`**kwargs`</b>:  Keyword arguments. 

Keyword Args: 
 - <b>`name`</b> (str):  The name of the function. Default is "undefined". 
 - <b>`type`</b> (str):  The type of the function. Default is "standard". 
 - <b>`main`</b> (bool):  Whether the function is the main function. Default is True. 
 - <b>`prompt`</b> (str):  The prompt for the function. Default is an empty string. 
 - <b>`output_type`</b> (str):  The output type of the function. Default is "string". 



**Returns:**
 
 - <b>`Function`</b>:  The created function object. 


---

<a href="..\python\platogaze.py#L659"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_variable`

```python
create_variable(*args, **kwargs)
```

Create a variable dictionary with the specified type, name, and value. 



**Args:**
 
 - <b>`*args`</b>:  Additional positional arguments (not used in this function). 
 - <b>`**kwargs`</b>:  Additional keyword arguments. 
 - <b>`type`</b> (str):  The type of the variable (default: "input"). 
 - <b>`name`</b> (str):  The name of the variable (default: "undefined"). 
 - <b>`value`</b> (str):  The value of the variable (default: ""). 



**Returns:**
 
 - <b>`dict`</b>:  A dictionary representing the variable. 


---

<a href="..\python\platogaze.py#L688"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create`

```python
create(type: str = 'program', *args, **kwargs)
```

Creates a new item of the specified type. 



**Args:**
 
 - <b>`type`</b> (str):  The type of item to create. Valid values are "program", "function", and "variable". 
 - <b>`value`</b> (dict):  The initial values of the item. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the type is unrecognized. 



**Returns:**
 The newly created item. 


---

<a href="..\python\platogaze.py#L709"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `link_to_program`

```python
link_to_program(program_dict: dict)
```

Recursively traverses the functions in the program_dict and links the programs. 



**Args:**
 
 - <b>`program_dict`</b> (dict):  The dictionary representing the program. 



**Returns:**
 
 - <b>`dict`</b>:  The updated program dictionary with linked programs. 


---

<a href="..\python\platogaze.py#L736"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `load_from_json`

```python
load_from_json(file_path: str) → Program
```

Load data from a JSON file and return a Program object. 



**Args:**
 
 - <b>`file_path`</b> (str):  The path to the JSON file. 



**Returns:**
 
 - <b>`Program`</b>:  The Program object created from the JSON data. 


---

<a href="..\python\platogaze.py#L763"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `fake_api_call`

```python
fake_api_call(prompt: str)
```






---

## <kbd>class</kbd> `Function`




<a href="..\python\platogaze.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(function_dict: dict) → None
```








---

<a href="..\python\platogaze.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `display`

```python
display()
```





---

<a href="..\python\platogaze.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_valid`

```python
is_valid(function_dict)
```

Check whether the function dictionary is valid. 



**Args:**
 
 - <b>`function_dict`</b> (dict):  The function dictionary to be validated. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the function dictionary is missing required keys. 



**Returns:**
 
 - <b>`bool`</b>:  True if the function dictionary is valid, False otherwise. 

---

<a href="..\python\platogaze.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `to_dict`

```python
to_dict()
```






---

## <kbd>class</kbd> `Program`




<a href="..\python\platogaze.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(program_dict: dict) → None
```

Initializes an instance of Program with a program dictionary. 



**Args:**
 
 - <b>`program_dict`</b> (dict):  A dictionary representing the program. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the program format is invalid. 




---

<a href="..\python\platogaze.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `wrapper`

```python
wrapper(*args, **kwargs)
```





---

<a href="..\python\platogaze.py#L319"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `add_function`

```python
add_function(new_function, id: str)
```

Adds a new function to the program identified by the given ID. 



**Args:**
 
 - <b>``new_function` (Function or dict)`</b>:  The new function to be added. It can be either a Function object or a dictionary representing the function. 
 - <b>`id`</b> (str):  The ID of the program where the function should be added. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the new_function parameter is not of type Function or dict. 



**Returns:**
 None 

---

<a href="..\python\platogaze.py#L289"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `add_program`

```python
add_program(new_program, id: str = '')
```

Adds a new program to the existing program list. 



**Args:**
 
 - <b>``new_program` (``Program`` or `dict`)`</b>:  The new program to be added. It can be either a `Program` object or a dictionary. 
 - <b>`id`</b> (str, optional):  The ID of the program whose functions will be appended. Consider the id as the folder's path. If not provided, a new program will be added to the root path. 



**Raises:**
 
 - <b>``TypeError``</b>:  If the new_program is not of type `Program` or dict. 



**Returns:**
 `None` 

---

<a href="..\python\platogaze.py#L348"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `add_variable`

```python
add_variable(item: dict, id: str)
```

Adds a variable to the program. 



**Args:**
 
 - <b>`item`</b> (dict):  The variable item to be added. Should be a dictionary. 
 - <b>`id`</b> (str):  The ID of the program. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the item is not a dictionary. 
 - <b>`ValueError`</b>:  If the variable type is invalid. 



**Returns:**
 None 

---

<a href="..\python\platogaze.py#L208"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `display`

```python
display(msg='')
```





---

<a href="..\python\platogaze.py#L183"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `download_on_change`

```python
download_on_change(method)
```

This method is a decorator for all methods that change the program object. It will automatically save the program to a file after the method is executed. 



**Args:**
 
 - <b>`method`</b> (function):  The method to be decorated. 

---

<a href="..\python\platogaze.py#L232"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_parent_program`

```python
get_parent_program(id: str)
```

Retrieves the parent program of the given ID. 



**Args:**
 
 - <b>``id` (str)`</b>:  The ID of the program. 



**Returns:**
 The parent program object. 

update function 1.2 

---

<a href="..\python\platogaze.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_program`

```python
get_program(id: str = '1')
```

Retrieves the program based on the given ID. 



**Args:**
 
 - <b>``id` (str)`</b>:  The ID of the program to retrieve. Defaults to "1". 



**Returns:**
 
 - <b>``dict``</b>:  The program corresponding to the given ID. 

---

<a href="..\python\platogaze.py#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_variable`

```python
get_variable(id: str) → dict
```

Retrieves a variable from the program based on its ID. 



**Args:**
 
 - <b>`id`</b> (str):  The ID of the variable in the format "program.variable_index". 



**Returns:**
 
 - <b>`dict`</b>:  The variable object. 



**Raises:**
 
 - <b>`IndexError`</b>:  If the program or variable index is out of range. 

---

<a href="..\python\platogaze.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_valid`

```python
is_valid(program_dict: dict)
```

Checks if the given program dictionary is valid. 



**Args:**
 
 - <b>`program_dict`</b> (dict):  The program dictionary to validate. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the program dictionary is missing any required keys or has invalid variable types. 



**Returns:**
 
 - <b>`bool`</b>:  True if the program dictionary is valid, False otherwise. 

---

<a href="..\python\platogaze.py#L265"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `read`

```python
read(id: str = '') → dict
```

Retrieves a program or function based on the given ID. 



**Args:**
 
 - <b>`id`</b> (str):  The ID of the program or function to retrieve. If try to read a variable, the id should be like "v1" (any variable type + variable id) 



**Returns:**
 
 - <b>`str or dict`</b>:  The program or function corresponding to the given ID. 

---

<a href="..\python\platogaze.py#L509"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `replace_variables`

```python
replace_variables(prompt: str, variables: list)
```

Replaces variables in the given prompt with their corresponding values. 



**Args:**
 
 - <b>`prompt`</b> (str):  The prompt string containing variables to be replaced. 
 - <b>`variables`</b> (list):  A list of dictionaries, where each dictionary contains the name and value of a variable. 



**Returns:**
 
 - <b>`str`</b>:  The prompt string with variables replaced by their values. 

---

<a href="..\python\platogaze.py#L598"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `run`

```python
run()
```

Runs the program. 



**Returns:**
  None 

---

<a href="..\python\platogaze.py#L540"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `run_function`

```python
run_function(function_dict: dict, variables)
```





---

<a href="..\python\platogaze.py#L582"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `run_program`

```python
run_program(program_dict: dict)
```

Recursively runs the program specified in the program_dict. 



**Args:**
 
 - <b>`program_dict`</b> (dict):  A dictionary containing the program to be executed. 



**Returns:**
 None 

---

<a href="..\python\platogaze.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `save_to_file`

```python
save_to_file()
```

Saves the program data to files. 

This method creates a folder named after the program name inside the 'download' folder. It then saves the program data in JSON format to separate files, including main.json and any linked program files. 



**Raises:**
 
 - <b>`KeyError`</b>:  If the 'name' key is not found in the properties dictionary. 



**Returns:**
 None 

---

<a href="..\python\platogaze.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `to_dict`

```python
to_dict()
```

Converts the program object to a dictionary. 



**Returns:**
 
 - <b>`dict`</b>:  A dictionary representation of the program object. 

---

<a href="..\python\platogaze.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `wrapper`

```python
wrapper(*args, **kwargs)
```





---

<a href="..\python\platogaze.py#L429"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update_function`

```python
update_function(new_function, id: str)
```

Update a function in the program with the given ID. 



**Args:**
 
 - <b>`new_function`</b> (Union[Function, dict]):  The new function to update. It can be either a Function object or a dictionary. 
 - <b>`id`</b> (str):  The ID of the function to update. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the new_function is not of type Function or dict. 



**Returns:**
 None 

---

<a href="..\python\platogaze.py#L404"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update_program`

```python
update_program(new_program, id: str = '')
```

Updates the program at the specified ID with the new program. 



**Args:**
 
 - <b>`new_program`</b> (Program or dict):  The new program to update with. 
 - <b>`id`</b> (str):  The ID of the program to update. Defaults to an empty string. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the new_program is not of type Program or dict. 



**Returns:**
 None 

---

<a href="..\python\platogaze.py#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update_variable`

```python
update_variable(item: dict, id: str = 'i1')
```

Updates a variable in the program based on the given item and ID. 



**Args:**
 
 - <b>`item`</b> (dict):  The dictionary containing the updated variable information. 
 - <b>`id`</b> (str, optional):  The ID of the variable to be updated. Defaults to "i1". 



**Raises:**
 
 - <b>`TypeError`</b>:  If the item is not a dictionary. 
 - <b>`ValueError`</b>:  If the variable type is invalid. 



**Returns:**
 None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

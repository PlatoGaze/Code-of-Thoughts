<!-- markdownlint-disable -->

<a href="..\python\platogaze.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `platogaze.py`




**Global Variables**
---------------
- **create_type_methods**

---

<a href="..\python\platogaze.py#L397"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_program`

```python
create_program(name: str = 'undefined')
```






---

<a href="..\python\platogaze.py#L404"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_function`

```python
create_function(function_dict: dict)
```






---

<a href="..\python\platogaze.py#L412"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_variable`

```python
create_variable(variable_dict: dict)
```






---

<a href="..\python\platogaze.py#L425"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L446"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `load_from_json`

```python
load_from_json(file_path: str) → Program
```






---

## <kbd>class</kbd> `Function`




<a href="..\python\platogaze.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(function_dict: dict) → None
```








---

<a href="..\python\platogaze.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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





---

<a href="..\python\platogaze.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `to_dict`

```python
to_dict()
```






---

## <kbd>class</kbd> `Program`




<a href="..\python\platogaze.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `wrapper`

```python
wrapper(*args, **kwargs)
```





---

<a href="..\python\platogaze.py#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L248"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L121"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `display`

```python
display()
```





---

<a href="..\python\platogaze.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `download_on_change`

```python
download_on_change(method)
```

This method is a decorator for all methods that change the program object. It will automatically save the program to a file after the method is executed. 



**Args:**

 - <b>`method`</b> (function):  The method to be decorated. 

---

<a href="..\python\platogaze.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_parent_program`

```python
get_parent_program(id: str)
```

Retrieves the parent program of the given ID. 



**Args:**

 - <b>`id` (str)</b>:  The ID of the program. 



**Returns:**
 The parent program object. 

update function 1.2 

---

<a href="..\python\platogaze.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L159"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_variable`

```python
get_variable(id: str) → dict
```





---

<a href="..\python\platogaze.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_valid`

```python
is_valid(program_dict: dict)
```





---

<a href="..\python\platogaze.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `save_to_file`

```python
save_to_file()
```





---

<a href="..\python\platogaze.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `to_dict`

```python
to_dict()
```

Converts the program object to a dictionary. 



**Returns:**

 - <b>`dict`</b>:  A dictionary representation of the program object. 

---

<a href="..\python\platogaze.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `wrapper`

```python
wrapper(*args, **kwargs)
```





---

<a href="..\python\platogaze.py#L329"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L304"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\python\platogaze.py#L354"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update_variable`

```python
update_variable(item: dict, id: str = 'i1')
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

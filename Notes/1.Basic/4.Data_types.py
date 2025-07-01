# Data types
# Data types are the classification or categorization of data items.
# It represents the kind of value that tells what operations can be performed on a particular data.
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.
# Since everything is an object in Python programming, data types are classes and variables
# are instances (objects) of these classes.


# Python has the following data types built-in by default, in these categories:

# Python Data Types:

# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type: NoneType

# Getting the Data Type
# What is Python type()  Function?
# To define the values ​​of various data types and check their data types we use the type() function.
# Consider the following examples.

# This code assigns variable ‘x’ different values of various data types in Python.
# It covers string, integer, float, complex, list, tuple, range, dictionary, set,
# frozenset, boolean, bytes, bytearray, memoryview, and the special value ‘None’ successively.
# Each assignment replaces the previous value, making ‘x’ take on the data type and value
# of the most recent assignment.

x = "Hello World"
print(x, "-", type(x))
x = 16
print(x, "-", type(x))
x = 0.5
print(x, "-", type(x))
x = 3 + 5j
print(x, "-", type(x))
x = ["Unknown", "Coder"]
print(x, "-", type(x))
x = ("Code", "Hacker")
print(x, "-", type(x))
x = range(10)
print(x, "-", type(x))
x = {"name": "harrish", "age": 23, "Qualification": "MCA"}
print(x, "-", type(x))
x = {"harrish", "23", "MCA"}
print(x, "-", type(x))
x = frozenset({"harrish", "23", "MCA"})
print(x, "-", type(x))
x = True
print(x, "-", type(x))
x = b"Harrish"
print(x, "-", type(x))
x = bytearray(4)
print(x, "-", type(x))
x = memoryview(bytes(6))
print(x, "-", type(x))
x = None
print(x, "-", type(x))

# Hello World - <class 'str'>
# 16 - <class 'int'>
# 0.5 - <class 'float'>
# (3+5j) - <class 'complex'>
# ['Unknown', 'Coder'] - <class 'list'>
# ('Code', 'Hacker') - <class 'tuple'>
# range(0, 10) - <class 'range'>
# {'name': 'harrish', 'age': 23, 'Qualification': 'MCA'} - <class 'dict'>
# {'MCA', 'harrish', '23'} - <class 'set'>
# frozenset({'MCA', 'harrish', '23'}) - <class 'frozenset'>
# True - <class 'bool'>
# b'Harrish' - <class 'bytes'>
# bytearray(b'\x00\x00\x00\x00') - <class 'bytearray'>
# <memory at 0x000001BC5F234B80> - <class 'memoryview'>
# None - <class 'NoneType'>


# Python Numeric Data type:
# In Python, numeric data type is used to hold numeric values.

# Integers, floating-point numbers and complex numbers fall under Python numbers category.
# They are defined as int, float and complex classes in Python.

# int - holds signed integers of non-limited length.
# float - holds floating decimal points and it's accurate up to 15 decimal places.
# complex - holds complex numbers.

# Python Modules
# Any text file with the .py extension containing Python code is basically a module. 
# A module can define functions, classes, and variables.
# Different Python objects such as functions, classes, variables, constants, etc., defined in one module can be
# made available to an interpreter session or another Python script by using the import statement. 
# A module can also include runnable code.
# we can use modules to separate codes in separate files as per their functionality.
# This makes our code organized and easier to maintain.


# Module is a file that contains code to perform a specific task.


# Creating a Module
# Shown below is a Python script containing the definition of sum() function. It is saved as calc.py.

def sum(x, y):
    return x + y

# Importing a Module
# We can now import this module and execute the sum() function in the Python shell.

# Example: Importing a Module
import calc
n = calc.sum(5, 5) 
print(n)  #10


# In the same way, to use the above calc module in another Python script, use the import statement.
# Every module, either built-in or custom made, is an object of a module class. 
# Verify the type of different modules using the built-in type() function, as shown below.

# Example: Module Type
import calc
print(type(calc))  # <class 'module'>

import math
print(type(math))  #<class 'module'>


# Renaming the Imported Module
# Use the as keyword to rename the imported module

# Example: 
import math as cal
n = cal.log(4) 
print(n) #1.3862943611198906


# from .. import statement
# The above import statement will load all the resources of the module in the current working environment 
# (also called namespace).
# It is possible to import specific objects from a module by using this syntax. 
# For example, the following module calc.py has three functions in it.

# calc.py
def sum(x,y):
    return x + y

def average(x, y):
    return (x + y)/2

def power(x, y):
    return x**y


# Now, we can import one or more functions using the from...import statement.


# Example: Importing Module's Functions
from calc import sum, average
n = sum(10, 20) #30
avg = average(10, 20) #15
p = power(2, 4)  #error


# You can also import all of its functions using the from...import * syntax.
# Example: Import Everythin from Module

from calc import *

n = sum(10, 20)
print(n)

avg = average(10, 20)
print(avg)

p = power(2, 4)
print(p)


# Module Search Path
# When the import statement is encountered either in an interactive session or in a script:

# First, the Python interpreter tries to locate the module in the current working directory.
# If not found, directories in the PYTHONPATH environment variable are searched.
# If still not found, it searches the installation default directory.
# As the Python interpreter starts, it put all the above locations in a list returned by the sys.path attribute.

# Example: Module Attributes
import sys
sys.path
['','C:\\python36\\Lib\\idlelib', 'C:\\python36\\python36.zip', 
'C:\\python36\\DLLs', 'C:\\python36\\lib', 'C:\\python36', 
'C:\\Users\\acer\\AppData\\Roaming\\Python\\Python36\\site-packages', 
'C:\\python36\\lib\\site-packages']

# If the required module is not present in any of the directories above, 
# the message ModuleNotFoundError is thrown.

# import MyModule
# Traceback (most recent call last): 
# File "<stdin>", line 1, in <module>
#     ModuleNotFoundError: No module named 'MyModule


# Reloading a Module
# Suppose you have already imported a module and using it. 
# However, the owner of the module added or modified some functionalities after you imported it. 
# So, you can reload the module to get the latest module using the reload() function of the imp module.

# Example: Reloading Module
import imp
imp.reload(calc)


# Getting Help on Modules
# Use the help() function to know the methods and properties of a module. 
# For example, call the help("math") to know about the math module. 
# If you already imported a module, then provide its name, e.g. help(math).

# You can also use the dir() function to know the names and attributes of a module.
# e.g: dir("math")

# Python Built-in modules
# There are several built-in modules in Python, which you can import whenever you like.

# importing built-in module math
import math

# using square root(sqrt) function contained 
# in math module
print(math.sqrt(25)) 

# using pi function contained in math module
print(math.pi) 

# 2 radians = 114.59 degrees
print(math.degrees(2)) 

# 60 degrees = 1.04 radians
print(math.radians(60)) 

# Sine of 2 radians
print(math.sin(2)) 

# Cosine of 0.5 radians
print(math.cos(0.5)) 

# Tangent of 0.23 radians
print(math.tan(0.23)) 

# 1 * 2 * 3 * 4 = 24
print(math.factorial(4)) 

# importing built in module random
import random

# printing random integer between 0 and 5
print(random.randint(0, 5)) 

# print random floating point number between 0 and 1
print(random.random()) 

# random number between 0 and 100
print(random.random() * 100) 

List = [1, 4, True, 800, "python", 27, "hello"]

# using choice function in random module for choosing 
# a random element from a set such as a list
print(random.choice(List)) 


# importing built in module datetime
import datetime
from datetime import date
import time

# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time()) 

# Converts a number of seconds to a date object
print(date.fromtimestamp(454554)) 


# references:
# https://www.geeksforgeeks.org/python-modules/
# https://www.programiz.com/python-programming/modules
# https://www.tutorialsteacher.com/python/python-module
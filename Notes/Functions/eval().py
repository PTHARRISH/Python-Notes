# eval():
# eval() is a built-in Python function that dynamically evaluates (executes)
# a Python expression passed to it as a string.

# It returns the result of the evaluated expression.

# Example:
result = eval("3 + 7")
print(result)  # Output: 10


# Why is it Useful?
# Allows you to interpret and execute code contained in strings at runtime.
# Useful when you need to process user input as code, evaluate mathematical formulas,
# or perform operations that aren't known until the program is running.

# How to Use eval()
# Basic Usage:
expression = "10 * (5 + 2)"
output = eval(expression)
print(output)  # Output: 70


# Using with Variables:
x = 5
result = eval("x + 10")
print(result)  # Output: 15

list1 = eval(input("enter list: "))
print("print a list using dynamic input ", list1)
print("print the type of my_list", type(list1))

# Real-World Use Cases
# Calculator Apps:
# If your program takes mathematical formulas as input
# (like from a GUI calculator),
# you can use eval() to compute the result.

# Dynamic Formula Evaluation:
# In spreadsheets or financial tools where users enter their own formulas.

# Configuration or Scripting:
# Some applications allow users or admins to script small behaviors
# using Python code snippets.

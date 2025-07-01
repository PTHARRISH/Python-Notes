# Python print() Function

# The print() function prints the specified message to the screen or other standard output device.
# The message can be a string or any other object. 
# The object will be converted into a string before written to the screen.
# The simplest way to produce output is using the print() function where you can pass zero or more expressions separated by commas.
# This function converts the expressions you pass into a string before writing to the screen.

# Syntax:
# print(object(s), sep=separator, end=end, file=file, flush=flush)

# Example:
# Printing a message on the screen:
print("Hello  World")
# Output:  Hello World

# Printing more than one object:
print("Hello", "how are you?")
# Output: Hello how are you?


# Printing a string variable:
a='Hello World'
print(a)
# Output: Hello World


# Printing a :
a='Hello World'
print(a)
# Output: Hello World



# Printing two variable:
a = 5
b = 7
print(a,b)
# output: 5 7


# Python end parameter in print()

# By default python’s print() function ends with a new line. 
# A programmer with C/C++ background may wonder how to print without a new line.
# Python’s print() function comes with a parameter called ‘end’. 
# By default, the value of this parameter is ‘\n’, i.e. the new line character. 
# You can end a print statement with any character/string using this parameter.

# ends the output with a <space> 
print("Welcome to" , end = ' ') 
print("CodingWorld", end = ' ') 
print()

# output: Welcome to CodingWorld

# ends the output with a <@> 
print("Welcome to" , end = '@') 
print("CodingWorld", end = '@') 
print() # next output will be print a newline 

# output: Welcome to@CodingWorld@


# Python sep parameter in print()

# The separator between the arguments to print() function in Python is space by default (soft space feature), 
# which can be modified and can be made to any character, integer, or string as per our choice. 
# The ‘sep’ parameter is used to achieve the same, it is found only in python 3.x or later. 
# It is also used for formatting the output strings.


# Example:
# Code for disabling the softspace feature
print('CodingWar', sep='')

# For formatting a date
print('08','11','2023', sep='-')

# Another example
print('Harrish','codingwarrior', sep='@')

# output:
# CodingWar
# 08-11-2023
# Harrish@codingwarrior

# Python file parameter in print()
# File parameter which specifies where values get printed to by default its Std out.

import io
dummyfile=io.StringIO('Hello, world!')
# print('Harrish',file=dummyfile)
print('Harrish',dummyfile.getvalue()) # Harrish Hello, world!
print(dummyfile.getvalue())


# The print() function in Python3 supports a file argument,
# which specifies where the function should write a given object(s) to. 
# If not specified explicitly, it is sys.stdout by default. It serves two essential purposes:
# Print to STDERR
# Print to external file
# Here’s an example of how to use the print() function to write a string to a file:

with open('filename.txt', 'w') as f:
    print('Harrish', file=f)

# Create a new StringIO object with an initial value
string_buffer = io.StringIO('Hello, world!')

# Write the contents of the buffer to a file-like object
print('Harrish', file=string_buffer)

# Get the value of the buffer
print(string_buffer.getvalue())


# Python flush parameter in print()
# The flush parameter is a Boolean value that specifies whether the output should be flushed immediately or not. By default, it is set to False.
# When flush is set to True, it forces the output to be written to the console immediately.
# Here’s an example:

import time

for i in range(5):
    print(i, end=' ', flush=True)
    time.sleep(0.5)

print('end')

# This will print the numbers 0 to 4 to the console, separated by spaces, 
# with a delay of 0.5 seconds between each number. 
# The flush=True parameter ensures that each number is printed immediately,
# rather than being buffered until the end of the loop.

# If the flush=False parameter numbers will printed after all value buffered then only display a value,
# The output will be display 2.0second after because time.sleep(0.5)sec.
# What is Programming?
# Programming is the process of writing instructions that a computer
# can follow to perform tasks like calculations,
# data processing, automation, etc.

# Think of it as writing a recipe for a computer.

# Example:
print("Hello, world!")
# You’re telling the computer:
# “Display the text ‘Hello, world!’ on the screen.”

# What is a Programming Language?
# A programming language is a way to communicate with a computer
# using specific keywords, rules, and symbols.
# Python is one such language—others include JavaScript, C++, Java, etc.
# Python is known for being:
# Easy to read
# Powerful
# Great for beginners and pros alike

# What is Programming Code?
# Programming Code (or source code) is the set of instructions
# you write to build a program.
# It's what the computer runs.

# Example:
name = "Alice"
print("Hello, " + name)
# This is a program written using Python code.


# What is Syntax?
# Syntax is the set of rules that define how you write code correctly
# in a programming language.

# Like grammar in English — you can’t write "are you how?"
# instead of "how are you?"

# Incorrect Syntax (will cause error):
# print "Hello"

# Correct Syntax:
print("Hello")

# What is Semantics?
# Semantics is the meaning behind your code.
# Syntax is how you write it; semantics is what it means.

# Example:
print("5" + "10")  # Output: "510"

# Correct syntax, but the semantics might be wrong if you expected addition
# (you got string concatenation instead).

# What is a Script?
# A script is a file with programming code (usually .py in Python)
# that runs line-by-line to perform tasks.

# You can run Python scripts to automate tasks like:
# Sending emails
# Renaming files
# Scraping websites

# Example (saved as hello.py):
# print("Running a script!")

# What is Automation?
# Automation means writing code to let the computer
# do tasks for you without manual effort.

# Example: Rename 1000 files instead of doing it one by one.

# Example:

for i in range(1, 4):
    with open(f"file{i}.txt", "w") as f:
        f.write("Created by script")


# What is a Function?
# A function is a reusable block of code that performs a task.


# Example:
def greet(name):
    print("Hello", name)


greet("John")  # Output: Hello John
# You define it once and can reuse it anywhere.

# What is a Variable?
# A variable is a container for storing data
# (like a label you stick on a value).

# Example:
age = 25
name = "Alice"
# Here, age holds a number, and name holds text.

# What is a Generic Label (Variable Name)?
# It’s just another way of referring to a variable name.
# Use clear, meaningful names.

# Example:
temperature = 98.6
username = "bob123"
# Avoid vague labels like x or data1 unless truly generic.

# What is print() in Python?
# The print() function displays output to the screen
# (like debugging or showing results).

# Example:
print("Hello!")

# What is an f-string?
# f-strings (formatted strings)
# let you insert variable values directly inside strings using {}.

# Example:
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Much cleaner than:

print("My name is " + name + " and I am " + str(age) + " years old.")

# What is Implicit Conversion?
# Python automatically converts data types when safe.

# Example:
x = 5  # int
y = 2.0  # float
result = x + y
print(result)  # Output: 7.0 (converted to float automatically)

# What is Explicit Conversion?
# You manually convert one data type to another using functions
# like int(), str(), float(), etc.

# Example:
age = "25"
age_num = int(age)  # Convert string to integer
print(age_num + 5)  # Output: 30

# What is an Expression?
# An expression is a piece of code that produces a value.

# Can be math, function calls, logic, etc.

# Example:
x = 5 + 3  # Expression: 5 + 3
print(len("hello"))  # Expression: len("hello")


# What is a Data Type?
# In Python (and all programming languages),
# a data type defines the kind of value a variable holds.
# Think of it like different types of containers:
# one for water (liquid), one for rice (solid), one for air (gas).
# You need the right container (or type) for the right content.

# In the same way, Python needs to know the type of data you're working with so
# it can handle it correctly — like doing math, storing text,
# looping through items, etc.

# Python Data Types (Main Categories)
# Python has several built-in data types. Here's a breakdown:

# 1. Numeric Types: For numbers
# a. int – Integer
# Whole numbers (positive, negative, or zero)

# Example:
age = 25

# b. float – Floating-point (decimal) number
# Numbers with decimal points

# Example:
# price = 99.99

# c. complex – Complex number (used in math)
# Numbers with real and imaginary parts

# Example:
# z = 3 + 5j

# 2. Text Type
# str – String
# A sequence of characters (letters, words, sentences)

# Written in quotes ' ' or " "

# Example:
name = "Alice"
greeting = "Hello, world!"

# 3. Boolean Type
# bool – Boolean
# Only two values: True or False
# Used in decision making (like if-statements)

# Example:
is_sunny = True
has_permission = False

# 4. Sequence Types
# These store collections of items.

# a. list – Ordered, changeable (mutable), allows duplicates

# Example:
fruits = ["apple", "banana", "cherry"]

# b. tuple – Ordered, unchangeable (immutable), allows duplicates

# Example:
dimensions = (1920, 1080)

# c. range – Sequence of numbers, usually used in loops

# Example:
numbers = range(5)  # same as [0, 1, 2, 3, 4]

# 5. Mapping Type
# dict – Dictionary
# Stores key-value pairs
# Unordered (as of Python 3.6+, it maintains insertion order)

# Example:
person = {"name": "John", "age": 30, "city": "New York"}

# 6. Set Types
# Used for storing unique items.
# a. set – Unordered, no duplicates

# Example:
colors = {"red", "green", "blue"}

# b. frozenset – Like a set, but unchangeable

# 7. Binary Types
# Used when working with binary data
# (e.g., files, images, or network communication).

# bytes

# bytearray

# memoryview

# Example:
data = b"Hello"  # bytes

# NoneType
# None – Special type that means “no value”
# Example:
x = None


# Table
# Data Type	    Example	                Description
# int	        42	                    Whole numbers
# float	        3.14	                Decimal numbers
# complex	    2 + 3j	                Complex numbers
# str	        "hello"	                Text/characters
# bool	        True, False	            True or False values
# list	        [1, 2, 3]	            Ordered, changeable sequence
# tuple	        (1, 2, 3)	            Ordered, unchangeable sequence
# dict	        {"key": "value"}	    Key-value pairs
# set	        {1, 2, 3}	            Unordered, unique elements
# frozenset	    frozenset([1, 2, 3])	Immutable set
# bytes	        b"abc"	                Binary data
# NoneType	    None	                No value

# How to Check a Variable’s Data Type
# You can use the type() function:

x = 10
print(type(x))  # Output: <class 'int'>

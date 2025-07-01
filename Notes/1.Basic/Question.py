# What is Programming?
# Programming is the process of writing instructions that a computer
# can follow to perform tasks like calculations, data processing, automation, etc.

# Think of it as writing a recipe for a computer.

# Example:
print("Hello, world!")
# You’re telling the computer: “Display the text ‘Hello, world!’ on the screen.”

# What is Syntax?
# Syntax is the set of rules that define how you write code correctly in a programming
# language.

# Like grammar in English — you can’t write "are you how?" instead of "how are you?"

# Incorrect Syntax (will cause error):
# print "Hello"

# Correct Syntax:
print("Hello")

# What is Programming Code?
# Programming Code (or source code) is the set of instructions you write to build a program.
# It's what the computer runs.

# Example:
name = "Alice"
print("Hello, " + name)
# This is a program written using Python code.

# What is a Programming Language?
# A programming language is a way to communicate with a computer using specific keywords, rules, and symbols.
# Python is one such language—others include JavaScript, C++, Java, etc.
# Python is known for being:
# Easy to read
# Powerful
# Great for beginners and pros alike

# What is Semantics?
# Semantics is the meaning behind your code.
# Syntax is how you write it; semantics is what it means.

# Example:
print("5" + "10")  # Output: "510"

# Correct syntax, but the semantics might be wrong if you expected addition (you got string concatenation instead).

# What is a Script?
# A script is a file with programming code (usually .py in Python) that runs line-by-line to perform tasks.

# You can run Python scripts to automate tasks like:
# Sending emails
# Renaming files
# Scraping websites

# Example (saved as hello.py):
# print("Running a script!")

# What is Automation?
# Automation means writing code to let the computer do tasks for you without manual effort.

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
# A variable is a container for storing data (like a label you stick on a value).

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
# The print() function displays output to the screen (like debugging or showing results).

# Example:
print("Hello!")

# What is an f-string?
# f-strings (formatted strings) let you insert variable values directly inside strings using {}.

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
# You manually convert one data type to another using functions like int(), str(), float(), etc.

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

# Keywords:
# Keywords in Python are reserved words that can not be used as a variable name,
# function name, or any other identifier.

# Get the List of all Python keywords
# Python code to demonstrate working of iskeyword() 

# importing "keyword" for keyword operations 
import keyword 


# printing all keywords at once using "kwlist()" 
print("The list of keywords is : ") 
print(keyword.kwlist) 
print("Totally ",len(keyword.kwlist)," in Python" )

# True, False, None Keyword

#     True: This keyword is used to represent a boolean true. If a statement is true, “True” is printed.
#     False: This keyword is used to represent a boolean false. If a statement is false, “False” is printed. 
#     None: This is a special constant used to denote a null value or a void. It’s important to remember, 0, any empty container(e.g. empty list) does not compute to None. 
#     It is an object of its datatype – NoneType. It is not possible to create multiple None objects and can assign them to variables.


# True, False, and None :

# Code :
print(False == 0) # return True, False value is always 0
print(True == 1) # return True 
print(True == 2)# return False because True value is 1

print(True + True + True) # 1+1+1=3 is output
print(True + False + False) # 1+0+0=1 is output

print(None == 0) # False
print(None == []) # False

# and, or, not, in, is

# and: 
#  This a logical operator in Python. “and” Return the first false value. If not found return last.

# example:
def oper():
    print(3 and 0) # 0
    print(3 and 10) # 10
    print(3 or 0) # 3
    print(3 or 10) # 3
oper()
# 3 and 0 return 0 . # Here 3 is True but 0 is False so it return False( 0 ) 
# 3 and 10 return 10 
# If both condition is True Then it will return True.
# if any condition is False then it will return False.

# or: 
#  This a logical operator in Python. “or” Return the first True value. if not found return last. 

# example:
def oper():
    print(3 or 0) # 3
    print(3 or 10) # 3
oper()

# 3 or 0 returns 3 
# 3 or 10 returns 3 
# 0 or 0 or 3 or 10 or 0 returns 3 
# If both condition is False Then it will return False.
# if any condition is True then it will return True.


# not: 
#   This logical operator inverts the truth value.
# in: 
#   This keyword is used to check if a container contains a value. This keyword is also used to loop through the container.
# is: 
#   This keyword is used to test object identity, i.e to check if both the objects take the same memory location or not. 

# Example: and, or, not, is and in keyword

# showing logical operation 
# or (returns True) 
print(True or False) 

# showing logical operation 
# and (returns False) 
print(False and True) 

# showing logical operation 
# not (returns False) 
print(not True) 

# using "in" to check 
if 's' in 'geeksforgeeks': 
	print("s is part of geeksforgeeks") 
else: 
	print("s is not part of geeksforgeeks") 

# using "in" to loop through 
for i in 'geeksforgeeks': 
	print(i, end=" ") 

print("\r") 

# using is to check object identity
# check the object address is same or not If the object address is same it wil return True or return false 
# string is immutable( cannot be changed once allocated) 
# hence occupy same memory location 
# print(' ' is ' ') 
a=10
b=10
print(a is b)# check the object address is same or not If the object address is same it wil return True or return false

# using is to check object identity 
# dictionary is mutable( can be changed once allocated) 
# hence occupy different memory location 
print({} is {}) 


# Iteration Keywords – for, while, break, continue

#  for: 
#   This keyword is used to control flow and for looping.

#  while: 
#   Has a similar working like “for”, used to control flow and for looping.

#  break: 
#   “break” is used to control the flow of the loop. 
#   The statement is used to break out of the loop and passes the control to the statement following immediately after loop.

# continue: 
#  “continue” is also used to control the flow of code. 
#   The keyword skips the current iteration of the loop but does not end the loop.

# Example: For, while, break, continue keyword

# Using for loop 
for i in range(10): 

	print(i, end=" ") # 0 1 2 3 4 5 6

	# break the loop as soon it sees 6 
	if i == 6: 
		break

print() 

# loop from 1 to 10 
i = 0
while i < 10: 

	# If i is equals to 6, 
	# continue to next iteration 
	# without printing 
	if i == 6: 
		i += 1
		continue
	else: 
		# otherwise print the value 
		# of i 
		print(i, end=" ") # 0 1 2 3 4 5 7 8 9 

	i += 1


# Conditional keywords – if, else, elif

#   if : It is a control statement for decision making. Truth expression forces control to go in “if” statement block.
#   else : It is a control statement for decision making. False expression forces control to go in “else” statement block.
#   elif : It is a control statement for decision making. It is short for “else if“

# Example: if, else, and elif keyword

# Python program to illustrate if-elif-else ladder 
#!/usr/bin/python 

i = 20
if (i == 10): 
	print("i is 10") 
elif (i == 20): 
	print("i is 20") 
else: 
	print("i is not present") 

# def

# def keyword is used to declare user defined functions.
# Example: def keyword

# def keyword 
def fun(): 
	print("Inside Function") 

fun() 

# Return Keywords – Return, Yield

#     return : This keyword is used to return from the function.
#     yield : This keyword is used like return statement but is used to return a generator.

# Example: Return and Yield Keyword

# Return keyword 
def fun(): 
	S = 0

	for i in range(10): 
		S += i 
	return S 


print(fun()) 

# Yield Keyword 


def fun(): 
	S = 0

	for i in range(10): 
		S += i 
		yield S 


for i in fun(): 
	print(i) 


# class

# class keyword is used to declare user defined classes.
# Example: Class Keyword

# Python3 program to 
# demonstrate instantiating 
# a class 


class Dog: 

	# A simple class 
	# attribute 
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method 
	def fun(self): 
		print("I'm a", self.attr1) 
		print("I'm a", self.attr2) 


# Driver code 
# Object instantiation 
Rodger = Dog() 

# Accessing class attributes 
# and method through objects 
print(Rodger.attr1) 
Rodger.fun() 


# With

# with keyword is used to wrap the execution of block of code within methods defined by context manager. This keyword is not used much in day to day programming.
# Example: With Keyword

# using with statement 
with open('file_path', 'w') as file: 
	file.write('hello world !') 


# as

# as keyword is used to create the alias for the module imported. 
# i.e giving a new name to the imported module. E.g import math as mymath.
# Example: as Keyword

import math as gfg 

print(gfg.factorial(5))


# pass

# pass is the null statement in python. 
# Nothing happens when this is encountered. 
# This is used to prevent indentation errors and used as a placeholder.
# Example: Pass Keyword

n = 10
for i in range(n): 

	# pass can be used as placeholder 
	# when code is to added later 
	pass


# Lambda

# Lambda keyword is used to make inline returning functions with no statements allowed internally. 
# Example: Lambda Keyword

# Lambda keyword 
g = lambda x: x*x*x 

print(g(7))

# Import, From

#   import : This statement is used to include a particular module into current program.
#   from : Generally used with import, from is used to import particular functionality from the module imported.

# Example: Import, From Keyword

# import keyword 
from math import factorial 
import math 
print(math.factorial(10)) 

# from keyword 
print(factorial(10))  # 3628800


# Exception Handling Keywords – try, except, raise, finally, and assert

#  try : This keyword is used for exception handling, 
#  used to catch the errors in the code using the keyword except. 
#  Code in “try” block is checked, if there is any type of error, except block is executed.
#  
#  except : As explained above, this works together with “try” to catch exceptions.
#  
#  finally : No matter what is result of the “try” block, block termed “finally” is always executed.
#  
#  raise: We can raise an exception explicitly with the raise keyword
#  
#  assert: This function is used for debugging purposes. 
#  Usually used to check the correctness of code. 
#  If a statement is evaluated to be true, nothing happens, but when it is false, “AssertionError” is raised. 
#  One can also print a message with the error, separated by a comma.

# Example: try, except, raise, finally, and assert Keywords




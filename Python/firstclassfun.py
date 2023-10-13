# First class functions

# First class objects in a language are handled uniformly throughout. 
# They may be stored in data structures, passed as arguments, or used in control structures. 
# A programming language is said to support first-class functions if it treats functions as first-class objects. 
# Python supports the concept of First Class functions.

# Properties of first class functions:

#     A function is an instance of the Object type.
#     You can store the function in a variable.
#     You can pass the function as a parameter to another function.
#     You can return the function from a function.
#     You can store them in data structures such as hash tables, lists, …

# Examples illustrating First Class functions in Python

# 1. Functions are objects: 
# Python functions are first class objects. 

# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() # Print Uppercase

  
print (shout('Hello')) # HELLO
print(shout) # Print the object of the function
yell = shout # assign a function to a variable and can be treated as objects 
print(yell) # print the object of the function shot and yell are same address yell -->shot
print (yell('Hello')) # HELLO

# In the above program we are assigning function to a variable
# This assignment doesn’t call the function. (yell=shot)
# It takes the function object referenced by shout and creates a second name pointing to it, yell.(yell -->shot)


# 2. Functions can be passed as arguments to other functions: 
# Because functions are objects we can pass them as arguments to other functions. 
# Functions that can accept other functions as arguments are also called higher-order functions. 


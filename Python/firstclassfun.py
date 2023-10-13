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

# Example 2:
def square(x):
    return x*x
f=square(5)
print(square) # print square functions object <function square at 0x7efca930fd90>
print(f) # 25
f=square # print the object of the function square and f are same address f -->square
print(f) # print square functions object <function square at 0x7efca930fd90>
print(f(5)) # 25


# 2. Functions can be passed as arguments to other functions: 
# Because functions are objects we can pass them as arguments to other functions. 
# Functions that can accept other functions as arguments are also called higher-order functions. 

# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): # the function was called from greet and it contains values on it
    return text.upper() 
  
def whisper(text): # the function was called from greet and it contains values on it
    return text.lower() 
  
def greet(func):# func - shout it will call the shout function 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function 
                    passed as an argument.""") # It will pass the argument to the func=shout,whisper
    print (greeting)  # print the returned functions value
  
greet(shout) # HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
greet(whisper) # hi, i am created by a function passed as an argument.

# In the example above, we have created a function greet which takes a function as an argument.

# Example 2:
def square(x):
    return x*x

def cube(x):
    return x*x*x

def myfunc(func,args):
    result=[]
    for i in args:
        result.append(func(i))
    return result

cubes=myfunc(cube,[1,2,3,4,5]) # cube name and list is passed to myfunc and it calls the cube function
print(cubes) # print cube functions value in list format [1, 8, 27, 64, 125]
squares=myfunc(square,[1,2,3,4,5]) # square name and list is passed to myfunc and it calls the square function
print(squares) # print square functions value in list format [1, 4, 9, 16, 25]

# 3. Functions can return another function: 
# Because functions are objects we can return a function from another function.

# Python program to illustrate functions 
# Functions can return another function 
  
def create_adder(x): # x=15 
    def adder(y): 
        print(x) # x=15 value will be passed inside adder function  
        return x+y 
  
    return adder # return the another function (adder)
  
add_15 = create_adder(15) 
print(add_15) # <function create_adder.<locals>.adder at 0x7f8aceb8a950> It return the function and locals object
print (add_15(10)) # It will pass the y=10 value it call the create_adder(15)and call the locals pass the value 10

#  In the above example, the create_adder function returns adder function.

# Example 2:

def logger(msg):
    def logmsg():
        print('log:',msg) # print global msg
    return logmsg # return local function on it
loghi=logger('Hi!') # pass the msg='Hi!' in logger function it will print inside a logmsg now logger function called and to print logmsg you need to call again
print(loghi) # <function logger.<locals>.logmsg at 0x7fb9fc8869e0>
loghi()

# Example 3:

def tags(tag):
    def wraptext(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wraptext
printh1=tags('h1') # It call the function pass the tag and it return local function you need to pass a value for locals
printh1('Hello') # you can pass various msg on it 
# Closure :
# Before seeing what a closure is, 
# we have to first understand what nested functions and non-local variables are. 

# What are Python Closures

# A Closure in Python is a function object that remembers values in enclosing scopes even 
# if they are not present in memory. 

# It is a record that stores a function together with an environment: a mapping associating each free variable 
# of the function (variables that are used locally but defined in an enclosing scope) with the value 
# or reference to which the name was bound when the closure was created.
# A closure—unlike a plain function—allows the function to access those captured variables 
# through the closure’s copies of their values or references, 
# even when the function is invoked outside their scope.


# example 1: This is not closure
def outerFunction(): 
	text='hi'
	def innerFunction(): 
		# text is free variable
		print(text) # text is free variable  it can be access inside a innerfunction 

	# Note we are returning function
	# WITH parenthesis
	return innerFunction() # returning and executing innerfunction


outerFunction() 

# Example 2:
# Python program to illustrate 
# closures 
def outerFunction():
	text='Hey' 

	def innerFunction(): 
		# text is free variable
		print(text) 

	# Note we are returning function
	# WITHOUT parenthesis it will not execute nothing
	return innerFunction 

myFunction = outerFunction() # It will execute everything inside a outerfunction and return innerFunction
print(myFunction) # myFunction is a function now because we only returned not execute the innerfunction 
print(myFunction.__name__)	# display inner function name on it
myFunction() # Hey
myFunction() # Hey
myFunction() # Hey

# It print out message. we are done with executing outer function. 
# but the inner function has still has access to that text variable that is it printing out.
# Thats what closure is In simple terms a closure is a inner function that remembers and has
# access to variable in the local scope in which it was created even after the outer function
# has finished executing

# Example 3: Add parameter to a function
def outerFunction(msg): 
	message=msg
	def innerFunction(): 
		print(message) 
	return innerFunction 

hi_Function = outerFunction('Hi!')
hello_Function = outerFunction('Hello!') 
hi_Function() # Hi!
hello_Function() # Hello!

# One thing you must notice that we stil innerfunction still doesnot take any argument
# to execute this function only need paranthesis.
# when call this each function print is own values 
# that closure closes over the free variable from their environment
# In this case message would be that free variable.


# Example 3:

import logging
logging.basicConfig(filename='example.log',level=logging.INFO) # create logging file

def logger(func):
	def logfun(*args): # *args= any no of arguments can be passed 
		logging.info('running"{}"with arguments {}'.format(func.__name__,args)) # print loggin info in example.log file on it
		print(func(*args)) # call those func name passed in outer function and pass the inner function *args values 
	return logfun # it only return the inner function not executed

def add(x,y):
	return x+y

def sub(x,y):
	return x-y

add_log=logger(add)# outer function executes and pass the argument
sub_log=logger(sub)

add_log(10,20) # inner function still have access to the outer function after execution it remember the inner function
add_log(3,3) # so it can easy to access the free variabe on it

sub_log(20,10)
sub_log(5,2)
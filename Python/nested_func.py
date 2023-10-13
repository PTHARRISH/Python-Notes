# Nested functions in Python

# A function that is defined inside another function is known as a nested function. 
# Nested functions are able to access variables of the enclosing scope. 

# In Python, these non-local variables can be accessed only within their scope and not outside their scope. 
# This can be illustrated by the following example: 

# Python program to illustrate
# nested functions

# global scope
def outerFunction(text):
    # enclosed scope
	def innerFunction():
		# local scope
		# non local variable
		print(text)

	innerFunction()

outerFunction('Hey!')

# As we can see innerFunction() can easily be accessed inside the outerFunction body but not outside of its body. 
# Hence, here, innerFunction() is treated as a nested Function that uses text as a non-local variable.
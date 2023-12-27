# Function Overloading: 
 

# As opposed to other languages (for example C++), method or function overloading is not supported in Python by default but that can be achieved in various ways.

 

# We can defined multiple functions with the same name but only the last function will be considered, all the rest gets hidden.

 

# Example:

 

# Method 1 (Not The Most Efficient Method):

def mult(a, b):
    print(a * b)
    
def mult(a, b, c):
    
    print(a * b * c)
    
    
mult(2, 4, 3)
# mult(2, 7)


# In the above code, there are two mult() methods, but the python compiler can only see the last i.e the one with 3 parameters. Therefore, even though we can define multiple methods with the same name and different arguments, but only the last method of them can be used. Calling any of the other methods will produce an error. Like here calling will mult(2,3) an error.

 

# This issue can be overcomed by the following method:

 

# Method 2 (Efficient One):
# By Using Multiple Dispatch Decorator 

 

# Multiple Dispatch Decorator Can be installed by: 

# Multiple Dispatch Decorator Can be installed by: 

# pip3 install multipledispatch
 

from multipledispatch import dispatch

@dispatch(int,int)
def mult(a, b):
    print(a * b)
    
@dispatch(int,int,int)    
def mult(a, b, c):
    print(a * b * c)
    
    
mult(2, 3, 5)
mult(2, 3)
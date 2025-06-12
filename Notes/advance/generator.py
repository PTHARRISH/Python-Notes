# Generator:
# In python Generator is a function that return an iterator that produces a sequence of value when iterated over.
# Generator are useful when we want to produce a large sequence of values but we don't want to store all of them in 
# memory at once.

# Create Python Generator:
# In python similiar to defining a normal function using the def keyword but instead of the return statement we
# use the yield statement.

# syntax:
# def generator_name(args):
#         yield something
# for value in generator_name():  
#     print(value)

# Here the yield keyword is used to produce a value from the generator.
# When the generator function is called it doesn't execute the function body immediately.
# Instead it return a generator object that can be iterated over to produce the value.

# Example:
print("-------------- Generator using for loop method --------------")
def mygenerator(n):
    value=0
    while value<n:
        yield value
        value+=1
for value in mygenerator(3):
    print(value) # 0 1 2

# In the above example the mygenerator() generator function takes an integer n as argument.
# When generator yields a value it keeps the state until the generator run again and yield the next value.
# Generator are iterator as well but the __iter__() and __next__() are created automatically we don't have to create
# them.
    
# Yield keyword that is used to generator function.
# A generator function is a type of function that memory efficient and and can be used like an iterator object.
# The yield keyword will turn any expression that is given with it into generator object and return it to the caller .
# Therefore you must iterate over the generator object.
    

# Generator :
print("-------------- Generator using next method --------------")
def myrange(start,end):
    current=start
    while current<end:
        yield current
        current+=1
    
nums=myrange(1,5)
print(next(nums)) # 1
print(next(nums)) # 2
print(next(nums)) # 3
# print(nums.__iter__()) # <generator object myrange at 0x000001B728EF0860>
print(nums.__next__()) # 4
# print(nums.__next__()) # StopIteration

# A generator is also an iterator, which means it supports the __iter__() and __next__() methods. 
# The __iter__() method returns the generator object itself, 
# and the __next__() method returns the next value from the generator.
# The next() method returns the next value from the iterator, or raises a StopIteration exception 
# if there are no more values.


# Python Generator Expression
# In Python, a generator expression is a concise way to create a generator object.
# It is similar to a list comprehension, but instead of creating a list, 
# it creates a generator object that can be iterated over to produce the values in the generator.

# Generator Expression Syntax
# A generator expression has the following syntax,
# (expression for item in iterable)

# Here, expression is a value that will be returned for each item in the iterable.
# The generator expression creates a generator object that produces the values of expression 
# for each item in the iterable, one at a time, when iterated over.

print("-------------- Python Generator Expression --------------")
# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)


# Here, we have created the generator object that will produce the squares of the numbers 0 
# through 4 when iterated over.
# And then, to iterate over the generator and get the values, we have used the for loop.

# Use of python generator
# 1. Easy to implement:
# Generator can be implemented in a clear and concise ways as compared to their iteraator class counter part.
# following example to implemented a sequence of power of 2 using iterator class

class powtwo:
    def __init__(self,max=0):
        self.n=0
        self.max=max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.max<self.n:
            raise StopIteration
        result=2**self.n
        self.n+=1
        return result

nums=powtwo(10)
for i in nums:
    print("power value is: ",i)

# The above program was lengthy and confusing generator.

# another method:
def powtwo1(max=0):
    n=0
    while n<max:
        yield 2**n
        n+=1

num1=powtwo1(10)
for i in num1:
    print("power of i: ",i)


# since generator keeps track of details automatically the implementation was concise and much cleaner.

# 2.memory efficient:
# A normal function to return a sequence will create the entire sequence in the memory before returning the result.
# This is an overkill if the number of items in the sequence is very large.
# Generator implementation of such sequence if memory friendly and is prefered 
# since it only produce one item at a time.

# 3. Represent Infinite Stream
# Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory,
# and since generators produce only one item at a time, they can represent an infinite stream of data.
# The following generator function can generate all the even numbers (at least in theory).

def all_even():
    n = 0
    while True:
        yield n
        n += 2

# 4. Pipelining Generators
# Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.
# Suppose we have a generator that produces the numbers in the Fibonacci series.
# And we have another generator for squaring numbers.
# If we want to find out the sum of squares of numbers in the Fibonacci series, 
# we can do it in the following way by pipelining the output of generator functions together.

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))

# Output: 4895
# Run Code
# This pipelining is efficient and easy to read (and yes, a lot cooler!).

# def generateFibonacciNumbers(n: int) -> List[int]: 
#     # Write your code here
#     a=0
#     b=1
#     d=1
#     while d<=n:
#         yield a
#         c = a + b
#         a = b
#         b = c
#         d+=1


# Here is a real-world example of using a generator and an iterator in Python. 
# Suppose you want to read a large file line by line, but you don’t want to load the whole file into memory. 
# You can use a generator function that yields each line of the file as an iterator. 
# Then you can iterate over the generator object using a for loop and process each line as you need.

# define a generator function that yields each line of a file
def read_file(filename):
    # open the file
    with open(filename, "r") as f:
        # loop through each line
        for line in f:
            # yield the line as an iterator
            yield line

# create a generator object by calling the generator function
lines = read_file("example.log")

# iterate over the generator object using a for loop
for line in lines:
    # print or process each line as you need
    print(line)

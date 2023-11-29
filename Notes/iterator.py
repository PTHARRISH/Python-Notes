# Python Iterator 
# Iterators are methods that iterate collections like list, tuple, dicts, and sets. 
# Something that can be looped over is called iterable.
# List is iterable we can loop over a list.

# Technically a python iterator object must implement to special methods.
# __iter__() , __next__() collectively called Iterator protocol. 

# 1. __iter__(): The iter() method is called for the initialization of an iterator. 
# This returns an iterator object.

# 2. __next__(): The next method returns the next value for the iterable. 
# When we use a for loop to traverse any iterable object, 
# internally it uses the iter() method to get an iterator object, 
# which further uses the next() method to iterate over. 
# This method raises a StopIteration to signal the end of the iteration.


# The Python iterators object is initialized using the iter() method. 
# It uses the next() method for iteration.
# using iter method we can loop through an object and return its elements.
# using next method we can use the next() to return the next item in the sequence.
# The iter() method returns an iterator object that represents a stream of data for the iterable object or 
# sentinel.


# Syntax:
# iter(object, sentinel)


# Parameters:
# 1. object: (Required) The object whose iterator should be created. 
# If the second parameter sentinel is not specified, 
# this object must be a collection object with the __iter__() method or the __getitem__() method 
# with integer arguments starting at 0. 
# If sentinel is given, then this must be a callable object. 
# The __next__() function returns a value from the collection on each call.
# 2. sentinel: (Optional) A value that indicates the end of sequence.


# Return Value:
# Returns an iterator object for the given object.

# Iterators are implicitly used whenever we deal with collections of data types such as list, tuple or string 
# (they are quite fittingly called iterables). 
# The usual method to traverse a collection is using the for loop, as shown below.


# Iterating over built-in iterable using iter() method
# Sample built-in iterators

print("Iterating over a list: ")
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
    
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
    
# Iterating over a String
print("\nString Iteration") 
s = "Geeks"
for i in s :
    print(i)
    
# Iterating over dictionary
print("\nDictionary Iteration") 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s %d" %(i, d[i]))

print("-----------------------------------------------")

# Iterable vs Iterator
# Python iterable and Python iterator are different. 
# The main difference between them is, iterable in Python cannot save the state of the iteration, 
# whereas in iterators the state of the current iteration gets saved.

# Note: Every iterator is also an iterable, but not every iterable is an iterator in Python. 

# Iterating on an Iterable
# Iterating on each item of the iterable.

# Iterating through an iterator
# In python we can use the next() function to return the next item in the sequence.

print("Iterating through an iterator: ")
list1=[4,7,0]
iterator=iter(list1) 
print(iterator) # <list_iterator object at 0x000001B31739EAD0>

# It prints list_iterator objects not a value
# print(next(list1)) # ERROR:'list' object is not an iterator. because list1 doesn't have next method.

# list is iterable but not an iterator.  
# list iterator have a next() or __next__()method.
# you cannot directly use next method It shows an error('list' object is not an iterator).

print(next(iterator)) # 4 get the first element of the iterator.
print(next(iterator)) # 7
print(next(iterator)) # 0
# print(next(iterator)) # StopIteration
print("-----------------------------------------------")
# In the code the iter() create an iterator from the list.
# The next() function to retrieve the element of the iterator in sequential order.
# If no more data to be returned StopIteration Exception occurred.

# Getting StopIteration Error while using iterator:
# Iterable in Python can be iterated over multiple times, 
# but iterators raise StopIteration Error when all items are already iterated.
# Here, we are trying to get the next element from the iterator after the completion of the for-loop. 
# Since the iterator is already exhausted, it raises a StopIteration Exception. 
# Whereas, using an iterable, we can iterate on multiple times using for loop or can get items using indexing.

# Example for iterator
print("Iterator using loops: ")
print("traverse a collection is using the for loop: ")
nums = [1, 2, 3, 4, 5] # create an iterator from the list
for item in nums:
    print(item)

# output: 
# 1
# 2
# 3
# 4
# 5
print("-----------------------------------------------")
# A more elegant way of automatically iterating is by using for loop.
# The for loop in python is used to iterate over the elements of the iterator untill it is exhausted.
# In the above example the for loop iterates over a list object- myList, and prints each individual element.
# This process continues untill the iterator is exhausted at which point the for loop terminates.  
# When we use a for loop to traverse any iterable object, internally it uses the iter() method.
  

print("using while loop: ")
def traverse(iterable):
    it=iter(iterable)
    while True:
        try:
            item=next(it)
            print(item)
        except StopIteration:
            break
arr=[10,20,21,30]
traverse(arr)
print("-----------------------------------------------")
# Instead of using the for loop as shown above, we can use the iterator function iter(). 
# The iterator object uses the __next__() method. 
# Every time it is called, the next element in the iterator stream is returned. 
# When there are no more elements available, the StopIteration error is raised.


print("Example: iter() and __next__()")
nums = [1, 2, 3, 4, 5]
iter = iter(nums) # returns an iterator object

print(iter.__next__()) # calling __next__() to get the first element
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
# print(iter.__next__()) # raise StopIteration error after last element
print("-----------------------------------------------")

# In the above example, we specified a list collection object, so the iter() function returns the iterator object. 
# Using the __next__() method of an iterator object, we can get each individual element of the collection. 
# After returning the last element, it raises the StopIteration error.

# Implementing the __iter__() Method in Custom Class

# The custom class can also be a collection class by implementing __iter__() and __next__() method 
# to get an iterator object and use it with the for loop, as shown below.

# __iter__() returns the iterator object itself. If required, some initialization can be performed.

# __next__() must return the next item in the sequence. On reaching the end, and in subsequent calls, 
# it must raise StopIteration.


print("Implementing the __iter__() Method in Custom Class")

class DataStore:
    def __init__(self, data):
        self.index = -1
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if(self.index == len(self.data)-1):
            raise StopIteration
        else:
            self.index +=1
            return self.data[self.index]

ds = DataStore([1,2,3,4,56])
for i in ds:
    print(i)


# Using Sentinel Parameter
# The sentinel parameter is used to indicate the end of the sequence. 
# However, the class must be callable, which internally calls __next__() method. 
# The following DataStore class is modified to demonstrate the use of the sentinel parameter 
# by adding __call__ = __next__.

# class Datastore:
# 	def __init__(self, data):
# 		self.index = -1
# 		self.data = data
# 	def __iter__(self):
# 		return self
# 	def __next__(self):
# 		if(self.index == len(self.data)-1):
# 		    raise StopIteration
# 		self.index +=1
# 		return self.data[self.index]
# 	__call__ = __next__
    
# ds = Datastore([1,2,3])
# itr = iter(ds, 3) # sentinel is 3, so it will stop when encounter 3
    
# for i in itr:
# 	print(i) # 1 2



# references
# https://www.programiz.com/python-programming/iterator
# https://www.geeksforgeeks.org/iterators-in-python/
# https://www.tutorialsteacher.com/python/iter-method
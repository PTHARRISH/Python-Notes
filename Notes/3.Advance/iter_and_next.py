# __iter__() and __next__():
# In many instances, we get a need to access an object like an iterator. 
# One way is to form a generator loop but that extends the task and time taken by the programmer. 
# Python eases this task by providing a built-in method __iter__() for this task. 

# Python __iter__()
# The __iter__() function in Python returns an iterator for the given object (array, set, tuple, etc..,). 
# It creates an object that can be accessed one element at a time using __next__() in Python, 
# which generally comes in handy when dealing with loops.

# Syntax:
# iter(object)
# iter(callable, sentinel)

# Object: 
# The object whose iterator has to be created. 
# It can be a collection object like a list or tuple or a user-defined object (using OOPS).

# Callable, Sentinel: 
# Callable represents a callable object, and sentinel is the value at which the iteration is needed to be terminated, 
# sentinel value represents the end of the sequence being iterated.

# Exception
# If we call the iterator after all the elements have been iterated, then StopIterationError is raised.
# The __iter__() in Python returns an iterator object that goes through each element of the given object. 
# The next element can be accessed through __next__() in Python. 
# In the case of the callable object and sentinel value, 
# the iteration is done until the value is found or the end of elements is reached. 
# In any case, the original object is not modified.

# In this example, 
# we are using the iter and next function to iterate through the list and print the next element in the next line.

# Python code demonstrating
# basic use of iter()
listA = ['a','e','i','o','u']

iter_listA = iter(listA)

try:
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA))
	print( next(iter_listA)) #StopIteration error
except:
	pass


# Python __next__():
# Python __next__() is responsible for returning the next element of the iteration. 
# If there are no more elements then it raises the StopIteration exception. 
# It is part of the iterable and iterator interface, which allows us to create custom iterable objects, 
# such as generators, and control how elements are retrieved one at a time from those iterables.

# In this example, we are using __next__() function in Python to iterate and print next element inside the list.

# Python code demonstrating
# basic use of iter()
lst = [11, 22, 33, 44, 55]

iter_lst = iter(lst)
while True:
	try:
		print(iter_lst.__next__()) 
	except:
		break

# In this example, we are using __next__() in Python to show the exception that is thrown if next element is not present.

# Python code demonstrating
# basic use of iter()

listB = ['Cat', 'Bat', 'Sat', 'Mat']
iter_listB = listB.__iter__()
try:
	print(iter_listB.__next__())
	print(iter_listB.__next__())
	print(iter_listB.__next__())
	print(iter_listB.__next__())
	print(iter_listB.__next__())
except:
	print(" \nThrowing 'StopIterationError'","I cannot count more.")


# User-defined objects (using OOPS) 
# In this example, we are using user defined objects along with defining __iter__() and __next__() functions 
# to show the use of iter() using OOPS in Python.
	
class Counter:
	def __init__(self, start, end):
		self.num = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self): 
		if self.num > self.end:
			raise StopIteration
		else:
			self.num += 1
			return self.num - 1
						
# Driver code
if __name__ == '__main__' :
	a, b = 2, 5
	c1 = Counter(a, b)
	c2 = Counter(a, b)
	
	# Way 1-to print the range without iter()
	print ("Print the range without iter()")
	
	for i in c1:
		print ("Eating more Pizzas, counting ", i, end ="\n")
	
	print ("\nPrint the range using iter()\n")
	
	# Way 2- using iter()
	obj = iter(c2)
	try:
		while True: # Print till error raised
			print ("Eating more Pizzas, counting ", next(obj))
	except: 
		# when StopIteration raised, Print custom message
		print ("\nDead on overfood, GAME OVER") 
		
        

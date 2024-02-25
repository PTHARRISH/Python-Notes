# Array:
# An array is a type of linear data structure 
# that is defined as a collection of elements with same or different data types. 
# They exist in both single dimension and multiple dimensions. 
# These data structures come into picture when there is a necessity 
# to store multiple elements of similar nature together(data type) at one place.

# The difference between an array index and a memory address 
# array index acts like a key value to label the elements in the array. 
# a memory address is the starting address of free memory available.

# Following are the important terms to understand the concept of Array.

# Element − Each item stored in an array is called an element.
# Index − Each location of an element in an array has a numerical index, which is used to identify the element.

# An array is a collection of items stored at contiguous memory locations.
# The idea is to store multiple items of the same type together. 
# This makes it easier to calculate the position of each element by simply adding an offset to a base value, 
# i.e., the memory location of the first element of the array (generally denoted by the name of the array).

# Creating an Array
# Array in Python can be created by importing an array module. 
# array(data_type, value_list) is used to create an array with data type and value list specified in its arguments. 

# There are thre ways to import array module:
# Using import (import array)
# Using import and call alias name (import array as arr)
# from modules import all methods ( from array import * )

# Some of the data types are mentioned below which will help in creating an array of different data types. 
# i - signed Int - allow positive and negative values
# I - unsigned Int - allow only positive values
# d - double - allow double values
# f - float - allow floating point values
# u - unicode character - allow unicode character values
# b - signed byte integer - allow positive and negative byte integer values
# B - unsigned byte integer - allow positive byte integer values only


from array import *

a=array('i',[-1,2,3,4,5])

print(a) # array('i', [1, 2, 3, 4, 5])

a=array('I',[1,2,3,4,5])

print(a) # array('I', [1, 2, 3, 4, 5])

# a=array('i',[1,2,3,4,5,'a'])

# print(a) # TypeError: 'str' object cannot be interpreted as an integer

# a=array('I',[-1,2,3,4,5])

# print(a) OverflowError: can't convert negative value to unsigned int

a=array('u',['a','b','c'])

print(a) # array('u', 'abc')

a=array('b',[-1,2,3,3]) # array('b', [-1, 2, 3, 3])

print(a) #TypeError: 'str' object cannot be interpreted as an integer

a=array('f',[-1,2,3,3.0]) # array('f', [-1.0, 2.0, 3.0, 3.0])

print(a) # convert int to float

a=array('d',[-1,2,3,3.00500050]) # array('d', [-1.0, 2.0, 3.0, 3.0050005])

print(a) # convert int to double

# a=array('B',[-1,2,3])

# print(a) # OverflowError: unsigned byte integer is less than minimum

# Array Operations and its Time complexity
# n - length of array, i - index
# Accessing - O(1)
# Inserting - Best O(1) Inserting at last, Worst O(n-i) Insert at any position
# Deleting  - Best O(1) Deleting at last, Worst O(n-i) Delete at any position
# Seaching  - Best O(1) got in first position, Average O(n-i) may got in middle ,Worst O(n) got at last postion


print("------------------------------------------ Adding Element to a array ------------------------------------------")
# Adding Elements to a Array
# Elements can be added to the Array by using built-in insert() function. 

# Insert():
# Insert is used to insert one or more data elements into an array. 
# a new element can be added at the beginning, end, or any given index of array. 

# append(): 
# append() is also used to add the value mentioned in its arguments at the end of the array. 


import array as arr
a = arr.array('i', [1, 2, 3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
	print(a[i], end=" ")
print()

a.insert(1, 4)
print("Array after insertion : ", end=" ")
for i in (a):
	print(i, end=" ")
print()

b = arr.array('d', [2.5, 3.2, 3.3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
	print(b[i], end=" ")
print()

b.append(4.4)
print("Array after insertion : ", end=" ")
for i in (b):
	print(i, end=" ")
print()


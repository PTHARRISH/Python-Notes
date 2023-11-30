# list - Introduction :

# In Python, a list is a built-in data structure that can store multiple items in a single variable. 
# Lists are ordered, mutable, and allow duplicate items. 
# They are one of the most versatile and commonly used data structures in Python, 
# and they are useful for a variety of tasks, 
# such as grouping together related data or storing sequences of elements.

# Characteristics of List:

# Ordered: The elements in a list have a specific order that is maintained.

# Mutable: You can modify the contents of a list after it has been created.

# Allows Duplicate Members: A list can have two or more elements that are identical.

# Heterogeneous: Lists can contain elements of different types, although this is generally not recommended for most applications.



# Creating Lists
# You can create a list by enclosing its elements in square brackets [], separated by commas:

my_list = [1, 2, 3, 4, 5]

# Or you can create an empty list and then add elements to it later:

my_list = []
my_list.append(1)
my_list.append(2)


# Accessing Elements
# You can access elements in a list by their index, starting from 0 for the first element:

first_element = my_list[0]  # Gets the first element (1 in this case)


# Modifying Elements
# As lists are mutable, you can change their elements:

my_list[0] = 10  # Changes the first element to 10


# Slicing Lists
# You can also take slices of lists to get new lists containing subsets of elements:

sub_list = my_list[1:4]  # Gets elements from index 1 to 3


# Useful Methods

# append(): Adds an element to the end of the list.

# clear(): Remove all items from the list.

# copy(): Return a copy of the list. 

# count(): Return the count of the number of items passed as an argument.

# extend(): Add all element of a list to another list.

# index(): Return the index of the first matched item.

# insert(): Adds an element at a specific index.

# pop(): Removes the element at a specific index.

# remove(): Removes the first occurrence of a value.

# reverse(): Reverses the list.

# sort(): Sorts the list.



# Example:
# Here's a small example that demonstrates some of these features:

# Creating a list
my_list = [1, 2, 3, 4, 5]
 
# Accessing elements
print(my_list[0])  # Output: 1
 
# Modifying elements
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]
 
# Slicing list
print(my_list[1:4])  # Output: [2, 3, 4]
 
# Using methods
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]


# Lists are an essential part of Python, and knowing how to use them effectively is crucial 
# for many programming tasks.

print("--------------------------------------------------------------------------")
print("                              List Exercises                              ")
print("--------------------------------------------------------------------------")
# 1.Printing a list

print("1.Printing a list")
list1=[3,10,5,28,63]
print(list1)
print("--------------------------------------------------------------------------")


# 2. In Python list can store different types of objects.
# Create a list containing the given elements: 3, 'spark', True, 0.5, None, 63 and assign to result variable.
# In response, print this variable to the console

print("2.Store different types of objects in list")
result=[3,'spark',True,0.5,None,63]
print(result)
print("--------------------------------------------------------------------------")


# 3.Create an empty list named result. Then, using the list.append() method, 
# add the following elements to the list: 34,1.5,True,'report.csv' In response, print this list to the console.

print("3.Create and add the following elements to the list")
result=[]
result.append(34)
result.append(1.5)
result.append(True)
result.append('report.csv')
print(result)
print("--------------------------------------------------------------------------")


# 4.Create an empty list named result. Then, using the list.insert() method, 
# add the following elements to the list (insert each element at the beginning of the list): 
# 34,1.5,True,'report.csv'.In response, print this list to the console.

print("4.Create and insert each element at the beginning of the list")
result=[]
result.insert(0,34)
result.insert(0,1.5)
result.insert(0,True)
result.insert(0,'report.csv')
print(result)
print("--------------------------------------------------------------------------")


# 5. The following list is given:
# techs = ['python', 'django', 'sql', 'html', 'css']
# Perform the following operations:
# insert 'git' at position with index 1
# insert 'aws' at the end of the list
# In response, print this list to the console.

print("5.Insert 'git' at position with index 1, insert 'aws' at the end of the list")
techs = ['python', 'django', 'sql', 'html', 'css']
techs.insert(1,'git')
techs.append('aws') # append method will insert element at the end of the list
# techs.insert(-1,'aws') # this will not show error but it will insert before last element
# techs.insert(6,'aws') # you can write its position or you use len function to insert at the last postion
# techs.insert(len(techs),'aws')
print(techs)
print("--------------------------------------------------------------------------")


# 6. The following list is given:
# techs = ['python', 'django', 'sql', 'html', 'css']
# Using the appropriate method pop the last element out and assign it to the result variable.
# In response, print the result and techs variables to the console as shown below.

# Output
# css
# ['python', 'django', 'sql', 'html']

print("6.Pop the last element out and assign it to the result variable")
techs = ['python', 'django', 'sql', 'html', 'css']
# print(techs[-1]) # print last element
result=techs.pop()
print(result) # to view the last deleted element is assign a variable and print it
print(techs)
print("--------------------------------------------------------------------------")


# 7. The following list is given:
# techs = ['python', 'django', 'sql', 'html', 'css']
# Using the appropriate method pop the item with index 1 out from the list and assign it to the result variable.
# In response, print the result and techs variables to the console as shown below.

# Expected result:
# django
# ['python', 'sql', 'html', 'css']

print("7.Pop the item with index 1 out from the list and assign it to the result variable")
techs = ['python', 'django', 'sql', 'html', 'css']
result=techs.pop(1)
print(result)
print(techs)
print("--------------------------------------------------------------------------")


# 8. Using the appropriate method, delete the first encountered element '0101'.
# In response, print the user_ids variable to the console.
# Expected result: ['0111', '1030', '0101', '3401', '0111', '1001']

print("8.Delete the first encountered element '0101'")
user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001']
user_ids.remove('0101') # use cannot use pop because it is str type it shows error 'str' object cannot be interpreted as an integer
print(user_ids) # remove method will remove the str on it
print("--------------------------------------------------------------------------")


# 9. The following list is given:
# user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001'] and the 
# user_id variable: user_id = '1040'
# When using the list.remove() method, attempting to remove a value that is not in the list results in a ValueError.
# Try to remove the user_id value from the user_ids list using the list.remove() method. 
# If the value is not in the list, print the following message to the console:
# "User with id '1040' is not in the list."
# Use try ... except ... clause in the solution.

# Expected result: User with id '1040' is not in the list.

print("9.Remove a value that is not in the list results in a ValueError")
user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001']
user_id = '1040'
try:
    user_ids.remove(user_id)
except ValueError:
    print(f"User with id '{user_id}' is not in the list.")
print("--------------------------------------------------------------------------")


# 10. The following list is given:
# techs = ['python', 'django', 'sql', 'html', 'css']
# Use the del statement to remove penultimate item from the techs list.
# In response, print the techs list to the console.

# Expected output: ['python', 'django', 'sql', 'css']

print("10.Remove penultimate item from the techs list")
techs=['python', 'django', 'sql', 'html', 'css']
del techs[-2] # del statement delete the particular element at the position negative index also support
print(techs) 
print("--------------------------------------------------------------------------")


# 11. The following list is given: techs = ['python', 'django', 'sql', 'html', 'c++', 'git', 'css']
# Using the del statement remove all items from the techs list except the first and last.
# In response, print the techs list to the console.
# Expected result: ['python', 'css']

print("11.Remove all items from the techs list except the first and last")
techs=['python', 'django', 'sql', 'html', 'css']
del techs[1:-1] # starting and ending value only displayed
# del techs[1:6] # del statement delete the particular element at the position of the index
print(techs)
print("--------------------------------------------------------------------------")


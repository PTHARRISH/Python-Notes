# Useful Methods
# Creating a list
my_list = [1, 2, 3, 4, 5]
print("------------------------------------------------------------------------------------------")
print("-------------------------------List methods-----------------------------------------------")
print("------------------------------------------------------------------------------------------")


# append(): Adds an element to the end of the list.
# syntax:
# list_name.append(values) # append any type of data

my_list.append(6)
print("Appending element in a list: ",my_list)  # 
# [10, 2, 3, 4, 5, 6] # 6 is appended
print("------------------------------------------------------------------------------------------")



# index(): Return the index of the first matched item.
# syntax:
# list_name.index(number)

print("Indexing element in a list: ",my_list.index(2))  
# return position value is 1

# print("Indexing element in a list ",my_list.index(22))  
# ValueError: 22 is not in list
print("------------------------------------------------------------------------------------------")



# insert(): Adds an element at a specific index.
# If the specified index is greater than max index then element will be inserted at last position.
# If the specified index is smaller than min index the element will be inserted at the first position.
# syntax:
# list_name.insert(position,values)
 
my_list.insert(3,99)
print("Inserting elements in a list: ",my_list) 
# [1, 2, 3, 99, 4, 5, 6] # 99 inserted

my_list.insert(10,100)
print("Inserting elements in a list: ",my_list) 
# [1, 2, 3, 99, 4, 5, 6, 100] # 100 inserted last position in a list

my_list.insert(-10,0)
print("Inserting elements in a list: ",my_list) 
# [0, 1, 2, 3, 99, 4, 5, 6, 100] # 0 inserted beginning position in a list
print("------------------------------------------------------------------------------------------")



# extend(): Add all element of a list to another list.
# syntax:
# list_name1.extend(list_name2) or list_name1.extend([values])
list1=[0,9,8,7]
my_list.extend(list1)
print("Extending elements in a list: ",my_list) 
# [1, 2, 3, 99, 4, 5, 6, 0, 9, 8, 7] # [0,9,8,7] extended

my_list.extend([1,2,3])
print("Extending elements in a list: ",my_list) 
# [0, 1, 2, 3, 99, 4, 5, 6, 100, 0, 9, 8, 7, 1, 2, 3] # [1,2,3] exetended

my_list.extend([[2,3]])
print("Extending elements in a Nested list: ",my_list) 
#  [0, 1, 2, 3, 99, 4, 5, 6, 100, 0, 9, 8, 7, 1, 2, 3, [2, 3]] # [2,3] nested list added

my_list.extend("HI")
print("Extending elements in a list: ",my_list) 
# [0, 1, 2, 3, 99, 4, 5, 6, 100, 0, 9, 8, 7, 1, 2, 3, [2, 3], 'H', 'I'] # 'H','I' added
print("------------------------------------------------------------------------------------------")



# pop(): Removes the element at a specific index.# position is optional, negative position also allowed.
# It returned removed element in the list.
# If the list is empty then pop() function raises IndexError
# syntax: list_name.pop(position) 

my_list.pop()
print("Popping elements in a list: ",my_list) 
# [0, 1, 2, 3, 99, 4, 5, 6, 100, 0, 9, 8, 7, 1, 2, 3, [2, 3], 'H'] # I is poped

print(my_list.pop(2)) # 2 # 2 is position 
print("Popping elements using position: ",my_list) 
# [0, 1, 3, 99, 4, 5, 6, 100, 0, 9, 8, 7, 1, 2, 3, [2, 3], 'H'] # 2 popped

print(my_list.pop(-3)) # 3
print("Popping elements using position: ",my_list)
# [0, 1, 3, 99, 4, 5, 6, 100, 0, 9, 8, 7, 1, 2, [2, 3], 'H'] # 3 popped

# my_list.pop(99)
# print("Popping elements using position: ",my_list) 
#  IndexError: pop index out of range

# list1=[]
# list1.pop()
# print("Popping elements using position: ",list1) 
#  IndexError: pop from empty list
print("------------------------------------------------------------------------------------------")



# remove(): Removes the first occurrence of a value.
# If the specified item not present in the list then we will get ValueError.
# It can't return any value.
# syntax: list_name.remove(values)

my_list.remove(99)
print("Removing elements in a list: ",my_list) 
# [0, 1, 3, 4, 5, 6, 100, 0, 9, 8, 7, 1, 2, [2, 3], 'H'] # 99 removed

# my_list.remove(16)
# print("Removing elements in a list: ",my_list) 
# ValueError: list.remove(x): x not in list
print("------------------------------------------------------------------------------------------")



# reverse(): Reverses the list.
# syntax: list_name.reverse()

my_list.reverse()
print("Reversing element in a list: ",my_list)
# ['H', [2, 3], 2, 1, 7, 8, 9, 0, 100, 6, 5, 4, 3, 1, 0] list is reversed
print("------------------------------------------------------------------------------------------")



# sort(): Sorts the list.
# we can sort according to reverse of default natural sorting order by using reverse=True argument.
# Here you can only sort the list of int only or str data only.
# syntax: list_name.sort(reverse=True) argument is optional.
# my_list=[1,2,3,'a','d','c'] # TypeError: '<' not supported between instances of 'str' and 'int' # invalid
# my_list=[1,2,3,[1,2]] # TypeError: '<' not supported between instances of 'list' and 'int' # invalid
my_list=[1,0,-1,8,2,3] # valid
# my_list=['a','d','c'] # valid
my_list.sort()
print("Sorting element in a list: ",my_list)
my_list.sort(reverse=True)
print("Sorting element in a list reverse argument: ",my_list)
print("------------------------------------------------------------------------------------------")



# count(): Return the count of the number of items passed as an argument.
my_list=[1,0,-1,8,2,3,1,0,-9] # valid
print("Counting element in a list: ",my_list.count(1))
my_list=['a','d','c','a','a'] # valid
print("Counting element in a list: ",my_list.count('a'))
print("------------------------------------------------------------------------------------------")



# copy(): Return a copy of the list. 
# syntax: list_name2=list_name.copy()
# Shallow Copy and Deep Copy
# A deep copy is a copy of a list, where we add an element in any of the lists, only that list is modified. 
# In list copy() method, changes made to the copied list are not reflected in the original list. 
# The changes made to one list are not reflected on other lists except for in nested elements (like a list within a list).
list1=my_list.copy()
list1[1]='hai'
print("Copying element in the old list:",my_list) # ['a', 'd', 'c', 'a', 'a']
print("Copying element in the old list and replacing new element: ",list1) # ['a', 'hai', 'c', 'a', 'a']
print("------------------------------------------------------------------------------------------")



# clear(): Remove all items from the list.
# syntax: list_name.clear()
print("Before clearing element in the list: ",my_list) # ['a', 'd', 'c', 'a', 'a']
my_list.clear()
print("After Clear element in the list: ",my_list) #  []
print("------------------------------------------------------------------------------------------")











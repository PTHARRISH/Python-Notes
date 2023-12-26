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
print("Appending element in a list ",my_list)  # Output: [10, 2, 3, 4, 5, 6]
print("------------------------------------------------------------------------------------------")



# index(): Return the index of the first matched item.
# syntax:
# list_name.index(number)
print("Indexing element in a list ",my_list.index(2))  # 1
print("------------------------------------------------------------------------------------------")



# insert(): Adds an element at a specific index.
# syntax:
# list_name.insert(position,values)
my_list.insert(3,99)
print("Inserting elements in a list ",my_list) # [1, 2, 3, 99, 4, 5, 6]
print("------------------------------------------------------------------------------------------")



# extend(): Add all element of a list to another list.
# syntax:
# list_name1.extend(list_name2) or list_name1.extend([values])
list1=[0,9,8,7]
my_list.extend(list1)
print("Extending elements in a list ",my_list) # [1, 2, 3, 99, 4, 5, 6, 0, 9, 8, 7] # [0,9,8,7] extended
# my_list.extend([0,9,8,7])
# print("Extending elements in a list ",my_list) # [1, 2, 3, 99, 4, 5, 6, 0, 9, 8, 7]
my_list.extend([[2,3]])
print("Extending elements in a Nested list ",my_list) #  [1, 2, 3, 99, 4, 5, 6, 0, 9, 8, 7, [2, 3]]
print("------------------------------------------------------------------------------------------")



# pop(): Removes the element at a specific index.
# syntax: list_name.pop(position) # position is optional, negative position also allowed
my_list.pop()
print("Popping elements in a list ",my_list) #  [1, 2, 3, 99, 4, 5, 6, 0, 9, 8, 7] # [2,3] popped
my_list.pop(2) 
print("Popping elements using position ",my_list) #  [1, 2, 99, 4, 5, 6, 0, 9, 8, 7] # 3 popped
my_list.pop(-3)
print("Popping elements using position ",my_list) #  [1, 2, 99, 4, 5, 6, 0, 8, 7] # 9 popped
print("------------------------------------------------------------------------------------------")



# remove(): Removes the first occurrence of a value.
# syntax: list_name.remove(values)
my_list.remove(99)
print("Popping elements in a list ",my_list) #  [1, 2, 3, 99, 4, 5, 6, 0, 9, 8, 7] # [2,3] popped





# clear(): Remove all items from the list.




# copy(): Return a copy of the list. 

# count(): Return the count of the number of items passed as an argument.




# reverse(): Reverses the list.

# sort(): Sorts the list.



# Example:
# Here's a small example that demonstrates some of these features:


# Using methods




# Lists are an essential part of Python, and knowing how to use them effectively is crucial 
# for many programming tasks.



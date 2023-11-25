# 1.Printing a list
list1=[3,10,5,28,63]
print(list1)


# 2. In Python list can store different types of objects.
# Create a list containing the given elements: 3, 'spark', True, 0.5, None, 63 and assign to result variable.
# In response, print this variable to the console
result=[3,'spark',True,0.5,None,63]
print(result)


# 3.Create an empty list named result. Then, using the list.append() method, 
# add the following elements to the list: 34,1.5,True,'report.csv' In response, print this list to the console.

result=[]
result.append(34)
result.append(1.5)
result.append(True)
result.append('report.csv')
print(result)


# 4.Create an empty list named result. Then, using the list.insert() method, 
# add the following elements to the list (insert each element at the beginning of the list): 
# 34,1.5,True,'report.csv'.In response, print this list to the console.

result=[]
result.insert(0,34)
result.insert(0,1.5)
result.insert(0,True)
result.insert(0,'report.csv')
print(result)


# 5. The following list is given:
# techs = ['python', 'django', 'sql', 'html', 'css']
# Perform the following operations:
# insert 'git' at position with index 1
# insert 'aws' at the end of the list
# In response, print this list to the console.

techs = ['python', 'django', 'sql', 'html', 'css']
techs.insert(1,'git')
techs.append('aws') # append method will insert element at the end of the list
# techs.insert(-1,'aws') # this will not show error but it will insert before last element
# techs.insert(6,'aws') # you can write its position or you use len function to insert at the last postion
# techs.insert(len(techs),'aws')
print(techs)


# 6. The following list is given:
# techs = ['python', 'django', 'sql', 'html', 'css']
# Using the appropriate method pop the last element out and assign it to the result variable.
# In response, print the result and techs variables to the console as shown below.

# Output
# css
# ['python', 'django', 'sql', 'html']

techs = ['python', 'django', 'sql', 'html', 'css']
# print(techs[-1]) # print last element
result=techs.pop()
print(result) # to view the last deleted element is assign a variable and print it
print(techs)


# 7. The following list is given:
# techs = ['python', 'django', 'sql', 'html', 'css']
# Using the appropriate method pop the item with index 1 out from the list and assign it to the result variable.
# In response, print the result and techs variables to the console as shown below.

# Expected result:
# django
# ['python', 'sql', 'html', 'css']

techs = ['python', 'django', 'sql', 'html', 'css']
result=techs.pop(1)
print(result)
print(techs)


# 8. Using the appropriate method, delete the first encountered element '0101'.
# In response, print the user_ids variable to the console.
# Expected result: ['0111', '1030', '0101', '3401', '0111', '1001']

user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001']
user_ids.remove('0101') # use cannot use pop because it is str type it shows error 'str' object cannot be interpreted as an integer
print(user_ids) # remove method will remove the str on it
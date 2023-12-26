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


# 12.The following list is given: record = ['01302', 'esmartdata', ['python', 'sql', 'git', 'css'], 30000]
# Iterate through the record list. If the object in the list is an instance of the list class, 
# remove all of its items. In response, print the contents of the record list to the console.
# Expected result: ['01302', 'esmartdata', [], 30000]

print("12.If the Object in the list is an instance of the list class, remove all of its items")
record = ['01302', 'esmartdata', ['python', 'sql', 'git', 'css'], 30000]

for items in record:
    if isinstance(items,list): # here list is class if list class present in item object it will clear a list. you can use other classes like int,str,tuple
        # isinstance is used to check the object in the list is an instance of the list class(object, class)
        items.clear()
print(record)
print("--------------------------------------------------------------------------")



# 13.The following list is given:

cities = [
    'Istanbul',
    'Moscow',
    'London',
    'Saint Petersburg',
    'Berlin',
    'Madrid',
]
# Find the index for 'Berlin' city using the appropriate method. 
# Then, using this index remove all elements to the end of the list, including the city named 'Berlin'.
# In response, print the cities list to the console.
# Expected result: ['Istanbul', 'Moscow', 'London', 'Saint Petersburg']
print("13.Find the index for 'Berlin' city and remove all elements to the end of the list ")
cities_list=cities.index('Berlin')
del cities[cities_list:]
print(cities)
print("--------------------------------------------------------------------------")


# 14.The following list is given:
countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]
# Use the appropriate method to find the number of occurrences of the word 'Russia' and print it on the console.
# Expected result: 2
print("14.find the number of occurrences of the word 'Russia")
print(countries.count('Russia'))
print("--------------------------------------------------------------------------")


# 15.The following lists are given:
countries_top_10 = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]

countries_next_5 = [
    'Austria',
    'Germany',
    'Romania',
    'Poland',
    'Hungary'
]
# Using the list.copy() method, make a shallow copy of the countries_top_10 list and assign it to the countries variable. Then, using the appropriate method, extend the countries list with the elements from the countries_next_5 list.
# In response, print the countries list to the console.
# Expected result:
# ['Turkey', 'Russia', 'United Kingdom', 'Russia', 'Germany', 'Spain', 'Ukraine', 'Italy', 'France', 'Belarus', 'Austria', 'Germany', 'Romania', 'Poland', 'Hungary']

print("15.make a shallow copy of the countries_top_10 list")
countries=countries_top_10.copy()
countries.extend(countries_next_5)
print(countries)
print("--------------------------------------------------------------------------")


# 16.The following list is given:
countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]

# Using the appropriate method, make a shallow copy of the countries list and assign it to the countries_copy variable. Then, using the appropriate method, reverse the order of elements in the countries_copy list. In response, print the index for the country named 'Italy' (countries_copy list) to the console.
# Expected result: 2
print("16.make a shallow copy of the countries list")
countries_copy=countries.copy()
countries_copy.reverse()
print(countries_copy.index('Italy'))
print("--------------------------------------------------------------------------")



# 17.The following list is given:
countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]

# Using the appropriate method, sort the elements of the countries list in ascending order.
# In response, print the first three items of the list to the console.
# Expected result: ['Belarus', 'France', 'Germany']
print("17.print the first three items of the list")
countries.sort()
print(countries[:3])
print("--------------------------------------------------------------------------")


# 18.The following list is given:

countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]
# Convert this list to the form below:
# ['SPA', 'ITA', 'FRA', 'UNI', 'BEL', 'TUR', 'GER', 'UKR', 'RUS', 'RUS']
# and assign to codes variable. (first three capital letters of the country name).
# Then sort in ascending order according to the last letter of the country code. In response, print this sorted list to the console.
# Expected result: ['SPA', 'ITA', 'FRA', 'UNI', 'BEL', 'TUR', 'GER', 'UKR', 'RUS', 'RUS']
print("18.Sort in ascending order according to the last letter of the country code")
codes=[countries1[:3].upper() for countries1 in countries]
codes.sort(key=lambda code:code[-1])
print(codes)
print("--------------------------------------------------------------------------")


# 19. The following list is given:
population = [
    ('Istanbul', 'Turkey', 15462452),
    ('Moscow', 'Russia', 12195221),
    ('London', 'United Kingdom', 9126366),
    ('Saint Petersburg', 'Russia', 5383890),
    ('Berlin', 'Germany', 3748148),
    ('Madrid', 'Spain', 3223334),
    ('Kyiv', 'Ukraine', 2950800),
    ('Rome', 'Italy', 2844750),
    ('Paris', 'France', 2140526),
    ('Minsk', 'Belarus', 1982444),
]

# Each item is a tuple that contains three pieces of information: city, country, and population.
# Sort the population list alphabetically by country name. Then, using a for loop, print each item to the console as shown below.

# Expected result:
# ('Minsk', 'Belarus', 1982444)
# ('Paris', 'France', 2140526)
# ('Berlin', 'Germany', 3748148)
# ('Rome', 'Italy', 2844750)
# ('Moscow', 'Russia', 12195221)
# ('Saint Petersburg', 'Russia', 5383890)
# ('Madrid', 'Spain', 3223334)
# ('Istanbul', 'Turkey', 15462452)
# ('Kyiv', 'Ukraine', 2950800)
# ('London', 'United Kingdom', 9126366)
print("19.Sort the population list alphabetically by country name")
population.sort(key=lambda row: row[1]) # row[1]->index[1] country name will pass in key lambda
for i in population:
    print(i)

print("--------------------------------------------------------------------------")


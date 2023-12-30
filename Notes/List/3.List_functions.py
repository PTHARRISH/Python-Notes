print("------------------------------------------------------------------------------------------")
print("---------------------------------Lists Function-------------------------------------------")
print("------------------------------------------------------------------------------------------")

n=[10,20,30,40]

# len(): return the number of elements present in the list.
# syntax: len(list) 
print("Length of the list: ",len(n))


# sum(): sum up the numbers in the list.
# syntax: sum(iterable numbers)
print("Sum of the list",sum(n))


# split(): split the strings and store it to a list
# syntax: list = string.split()
# lst=[]
# # input the list as string
# string = input("Enter elements (Space-Separated): ")
# # split the strings and store it to a list
# lst = string.split()  
# print('The list is:', lst)  


# # input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]

# # printing the list
# print('The list is:', lst) 



# reversed(): The reversed() function returns a reverse iterator, 
# which can be converted to a list using the list() function.
n=[1, 2, 3, 4, 5]
reversed_list=list(reversed(n)) # without list function it return reversed object
print("Reversed element ",reversed_list) # [5, 4, 3, 2, 1]


# reduce():
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all 
# of the list elements mentioned in the sequence passed along.
# This function is defined in “functools” module.



# 3.Display your name and age
# method 1:
def display_name_age(name,age):
    print(f'Hi {name} ! and your age is {age}.')
    
name,age = input('Enter your name and age with Double white space: ').split('  ')
display_name_age(name,age)

# Output:
# Enter your name and age with Double white space: Harrish P T  23
# Hi Harrish P T ! and your age is 23.


# Assignment 3:
# Display your address and your marks
def display_address_mark(address,mark):
    print(f'Your Address is {address} and your mark is {mark}')

address,mark = input('Enter the Address and your mark with Double white space: ').split('  ')
display_address_mark(address,mark)

# Output:
# Enter the Address and your mark with Double white space: new street  431
# Your Address is new street and your mark is 431

# Total Time Complexity:

#     Reading the input takes O(n)O(n) time.
#     Splitting the input string takes O(n)O(n) time.
#     Printing the output takes O(1)O(1) time.

# Thus, the overall time complexity of the code is:
# O(n)+O(n)+O(1)=O(n)

# Where n is the length of the input string. 
# So, the time complexity of this program is O(n).
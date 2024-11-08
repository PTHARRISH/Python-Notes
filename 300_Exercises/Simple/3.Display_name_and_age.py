# 3.Display your name and age
# method 1:
def display_name_age(name,age):
    print(f'Hi {name} ! and your age is {age}.')
    
name,age = input('Enter your name and age with Double white space: ').split('  ')
display_name_age(name,age)

# Output:
# Enter your name and age with Double white space: Harrish P T  23
# Hi Harrish P T ! and your age is 23.


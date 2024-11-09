# Take age from user and check age is eligible for voting
# Task 4:
def voting_age(name,age):
    if age >= 18 and age <= 100:
        print(f'Hi {name}!. You are eligible for voting your age is {age}')
    else:
        print(f'Hi {name}!. You are not eligible for voting !!')

try:
    name,age=input('Enter the name and age with single whitespace: ').split(' ')
    voting_age(name,int(age))
except ValueError:
    print('Enter the valid input')

# Output:
# Enter the name and age with single whitespace: Harrish 19
# Hi Harrish!. You are eligible for voting your age is 19


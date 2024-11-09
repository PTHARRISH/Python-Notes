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


# Assignment 4:
# Calculate the average mark and check eligible fo admission or not
def admission_mark(name,marks):
    marks = list(map(int, marks))
    subject=len(marks)
    total_mark=sum(marks)
    avg=total_mark//subject
    if avg>60:
        print(f'Hi {name}!. you are eligible for taking admission your score is {avg}')
    else:
        print(f'Hi {name}!. Sorry you are not eligible for taking admission still you need {60-avg} marks')
    
try:
    user_data = input('Enter the name after enter two whitespaces for marks single space:').split() 
    name=user_data[0]
    marks=user_data[1:]
    admission_mark(name,marks)
except ValueError:
    print('please enter the valid input')

# Output:
# Enter the name after enter two whitespaces for marks single space:Harrish 100 100 100 0
# Hi Harrish!. you are eligible for taking admission your score is 75

# Time Complexity:
#     map(int, marks): O(n)
#     sum(marks): O(n)
#     Other operations (len(), division, comparison, and printing): O(1)
# Thus, the overall time complexity of the function is dominated by the map() and sum() operations, 
# both of which have O(n) complexity.

# Time Complexity: O(n), where n is the number of marks in the input.
# Python Program to check if a Number Is Positive Or Negative

# Method 1: Using Brute Force
# This method uses Brute Force to check whether a given integer is Positive or Negative.

num=16
if num>0:
    print(f'{num} is a positive integer '.format(num))
elif num<0:
    print(f'{num} is a negative integer '.format(num))
else:
    print('Zero')


# Method 2: Using Nested if-else Statements
# This method uses a nested if-else Statements to check whether a given number is Positive or Negative.

if num>=0:
    if num==0:
        print('Zero')
    else:
        print(f'{num} is a positive integer '.format(num))
else:
    print(f'{num} is a negative integer '.format(num))


# Method 3: Using Ternary Operator
# This method uses a ternary operator to check whether a number is Positive or Negative.
num=0
# print("Positive" if num>=0 else "Negative")
print("Positive" if num>0 else "Negative" if num<0 else "zero")


if num>0:
    print("positive")
else:
    if num<0:
        print("negative")
    else:
        print("zero")

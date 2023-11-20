# Find the Sum of Numbers in a given Range in Python
# Method 1: Using Brute Force
# In this method we’ll use loops like for, while and do while to sum all the numbers that lay in the intervals of the given input integers.
def sum_of_natural(x,y):
    sum=0
    for i in range(x,y+1):
        sum+=i
    return sum
x=int(input('enter the starting number: '))
y=int(input('enter the ending number: '))
print(sum_of_natural(x,y))


# Method 2: Using the Formula
# In this method we’ll use formula mentioned below to find the sum of all the numbers that lay in the interval given by the input variable.
def sum_of_range(x,y):
    a=(((y*(y+1))//2)-(x*(x+1)//2)+x)
    print(a)

x=int(input('enter the starting number: '))
y=int(input('enter the ending number: '))
sum_of_range(x,y)


# Method 3: Using Recursion
# In this method we’ll use recursion to find the sum of all the numbers that lay in the interval given by the input variable. To know more about recursion, refer to Recursion in Python.
def sum_of_range(sum,x,y):
    if x>y:
        return sum
    return x+sum_of_range(sum,x+1,y)

sum=0
x=int(input('enter the starting number: '))
y=int(input('enter the ending number: '))
print(sum_of_range(sum,x,y))

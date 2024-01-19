# Find the Sum of First N Natural Numbers
# Method 1 : Using for Loop
# In this method we’ll add all the natural numbers until the given integer input using for loop in Python.
def sum_of_natural(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
n=int(input('enter the n number: '))
print(sum_of_natural(n))


# Method 2 : Using Formula for the Sum of Nth Term
# In this Method we use the formula for finding the sum of N term.
def sum_of_range(n):
    a=(n*(n+1))//2
    print(a)

n=int(input('enter the n number:'))
sum_of_range(n)


# Method 3 : Using Recursion
# This method uses Recursion to recursively add the natural numbers up to the given integer input using recursion in c++.

def sum_of_natural(n):
    if n==1:
        return 1
    return n+sum_of_natural(n-1)
n=int(input('enter the n number: '))
print(sum_of_natural(n))


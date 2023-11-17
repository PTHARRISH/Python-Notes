# factorial using Recursion
def factorial(n):
    return 1 if n==0 or n==1 else n*factorial(n-1)

n=5
print(f'the factorial of {n} is ',factorial(n))
# Time Complexity: O(n)

# factorial using in-built function
import math
 
def factorial(n):
    return(math.factorial(n))
 
n=5
print(f'the factorial of {n} is ',factorial(n))
# Time complexity: O(1)

# factorial using loop function
def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result

n=6
print('The factorial of {0} is {1}'.format(n,factorial(n)))
# Time Complexity: O(n)
# Check Prime Number or not
# using inbuilt function
from sympy import *
a=isprime(int(input('Enter a number : ')))
print(a)
# Time Complexity: O(sqrt(n))

# using for loop
def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            print(n,' is not an prime number')
            break
    else:
        print(n,' is a prime number')

n=int(input('enter the number: '))
prime(n)
# Time complexity: O(n)


# Method 1: Using Simple Iteration
n=int(input("Enter the number: "))
n1=0
n2=1
for i in range(2,n+1):
    n3=n1+n2
    n1=n2
    n2=n3
print(n3)

# Method 2: Using Recursive Function

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
n=int(input("Enter the number: "))
print(fib(n))


#factorial using Recursion
def factorial(n):
    return 1 if n==0 or n==1 else n*factorial(n-1)

n=5
print(f'the factorial of {n} is ',factorial(n),)
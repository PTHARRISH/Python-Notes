# Method 1: Using Simple Iteration
num=int(input())
reverse=0
while num!=0:
    remainder=num%10
    reverse=(reverse*10)+remainder
    num=num//10
print(reverse)



# Method 2: Using String Slicing

a=input()
print(a[::-1])


# Method 3: Using Recursion

def recurse(n,reverse):
    if n==0:
        return reverse
    else:
        remainder=n%10
        reverse=(reverse*10)+remainder
        return recurse(n//10,reverse)
    
n=int(input('enter the number: '))
reverse=0
print(recurse(n,reverse))
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

n=int(input("enter fibonnacci: "))
gen=fibonacci()
for i in range(n):
    print(next(gen))


print("-----------------------------------------------------------")
print("Fibonnaci Using Arithmetic Operations")

def fibonnacci(n):
    a=0
    b=1
    i=1
    while True:
        if i<n:
            temp=a+b
            a=b
            b=temp
            i+=1
            print(a)
        else:
            break

n=int(input("enter fibonnacci: "))
fibonnacci(n)

print("-----------------------------------------------------------")
print("Fibonnaci Using temp variable")

def fib(n):
    a,b=0,1
    for _ in range(n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c


n=int(input("number: "))
fib(n)


a = 0
b = 1
for i in range(n):
    for j in range(i+1): 
            print(a, end=" ")
            c = a + b
            a = b
            b = c
    print()

n = int(input())
# n=k+1
a=0
b=1
for i in range(0, n+1):
    for j in range(0, n - i):
        print(" ", end="")
    for j in range(0, i + 1):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()
    # n = n - 1
# n = k+1
for i in range(0, n):
    for j in range(0, i+1):
        print(" ", end="")
    for j in range(0, n - i):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()

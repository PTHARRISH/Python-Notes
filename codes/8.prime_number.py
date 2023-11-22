# Method 1: Simple iterative solution
n=int(input("enter the number: "))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("The {} is not a prime number".format(n))
else:
    print("The {} is a prime number".format(n))
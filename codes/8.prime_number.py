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


# Method 2: Basic Recursion technique
num=int(input("enter the number: "))
def checkPrime(num,iter=2):
  if num == iter:
    return True
  if num%iter==0:
    return False
  if num<2:
    return False
  return checkPrime(num,iter+1)
if checkPrime(num)==True:
   print("The {} is not a prime number".format(num))
else:
    print("The {} is a prime number".format(num))
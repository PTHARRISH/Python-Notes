# count divisor calcuate the 1 to n number divisible by its times
n=int(input("enter the number: "))
ans=0
for i in range(1,n+1):
    ans+=n//i  
print(ans)

# Explanation:
# n=1, n=2, n=3, n=4 n=5
# 1*1=1, 2*1=2,1*2=2, 3*1=3,1*3=3, 4*1=4,2*2=4,1*4=4, 1*5=5,5*1=5 =1("1")+2("2")+2("3")+3("4")+2("5")=10

# Easy way
# n/i
# 5//1=5, 5//2=2, 5//3=1, 5//4=1, 5//5=1 = 5+2+1+1+1 =10
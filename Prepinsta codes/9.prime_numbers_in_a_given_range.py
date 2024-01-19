# prime-numbers-in-a-given-range
# Method 1: Using inner loop Range as [2, number-1]

low,high=map(int,input('enter the starting and ending value: ').split(','))
primes=[]
for i in range(low,high+1):
    flag=0
    if i<2:
        continue
    if i==2:
        primes.append(i)
        continue
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        primes.append(i)

print(primes)


# Method 2: Using inner loop Range as [2, number/2]


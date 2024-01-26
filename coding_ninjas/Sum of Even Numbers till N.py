# Using brute force
def sum_of_even(n):
    sum=0
    for i in range(0,n+1):
        if i%2==0:
            sum+=i
    print(sum)

sum_of_even(int(input('Enter the number: ')))

# using while loop
def sum_of_even(n):
    sum=0
    i=0
    while i<=n:
        if i%2==0:
            sum+=i
            i+=2
    
    print(sum)

sum_of_even(int(input('Enter the number: ')))

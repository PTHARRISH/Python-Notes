# Armstrong number or not
# using For loop
def armstrong(num):
    num_to_str=str(num)
    n=len(num_to_str)
    sum=0
    for i in num_to_str:
        sum+=int(i)**n
    if sum==num:
        return(f'{num} is an Armstrong Number')
    return(f'{num} is not an Armstrong Number')

n=int(input('Enter the Armstrong Number: '))
print(armstrong(n))
# Time complexity: O(n), wheer n is length of number


# using while loop

def armstrong(n): 
    s = n 
    b = len(str(n))
    sum1 = 0
    while n != 0:
        r = n % 10
        sum1 = sum1+(r**b)
        n = n//10
    if s == sum1:
        print("The given number", s, "is armstrong number")
    print("The given number", s, "is not armstrong number")

n=int(input('Enter the Armstrong Number: '))
print(armstrong(n))
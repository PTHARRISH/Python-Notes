# 10.Sum of digit of a number
# using Sum function
num="123"
abc=list(map(int,num))
print("Sum of the str: ",sum(abc))


# Using String Character Extraction 
num=input("enter the number: ")
sum=0
for i in num:
    sum+=int(i)
print(sum)


# Using Brute Force
num=int(input("enter the number: "))
sum=0
while num!=0:
    digit=num%10
    sum+=digit
    num=num//10
print(sum)

# Using Recursion I
def sum_of_digit(num,sum):
    if num==0:
        return sum
    digit=num%10
    sum+=digit
    return sum_of_digit(num//10,sum)

num=int(input("enter the number: "))
sum=0
print(sum_of_digit(num,sum))


# Using Recursion II
def sum_of_digit(num):
    if num==0:
        return 0
    return num%10+sum_of_digit(num//10)

num=int(input("enter the number: "))
print(sum_of_digit(num))



# Using One Line Recursion 
def sum_of_digit(num):
    return 0 if num==0 else num%10 +sum_of_digit(num//10)

num=int(input("enter the number: "))
print(sum_of_digit(num))
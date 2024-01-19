# odd_or_even
# Method 1 : Using Brute Force
# This method simply checks if the given input integer is divisible by 2 or not. If it’s divisible then print Even or Odd otherwise.
num=int(input('enter the num: '))
if num % 2 == 0: 
  print("Given number is Even") 
else: 
  print("Given number is Odd")


# Method 2 : Using Ternary Operator
# This Method uses the ternary operator to check if the integer input is divisible by 2, If true print Even or Odd otherwise.
print("Even") if num%2 == 0 else print("Odd")


# Method 3 : Using Bitwise Operator without % operator
# This Method uses bitwise operators to check if a given number is Even or Odd.
def odd_or_even(n):
    if n&1==1:
        return f'{n} is odd number'
    return f'{n} is even number'
print(odd_or_even(19))


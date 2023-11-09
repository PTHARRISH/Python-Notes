# maximum_of_two_numbers
def maximum_two_numbers(a,b):
    if a<b:
        return b
    return a

a=5
b=4
print(maximum_two_numbers(a,b))

# Use Ternary operator
print(a if a>=b else b)

# Use Lambda function
c=lambda a,b:a if a>b else b
print(c(a,b))
def add(a,b):
    return a+b
a=10
b=20
print(add(a,b))

# Without using (+) operator
import operator
sum=operator.add(a,b)
print(sum)
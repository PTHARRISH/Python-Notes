# odd_or_even_without_%_operator
def odd_or_even(n):
    if n&1==1:
        return f'{n} is odd number'
    return f'{n} is even number'
print(odd_or_even(19))

a=[1,2,3]
b=a
print(a is b,a==b)
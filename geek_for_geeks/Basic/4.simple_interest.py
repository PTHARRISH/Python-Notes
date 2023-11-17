# Simple Interest
# Simple Interest = (p*n*r)/100 
# Where, 'p' is the principal amount 'n' is the time and 'r' is the rate


def simple(p,n,r):
    print('The principal is', p)
    print('The time period is', n)
    print('The rate of interest is',r) 
    si = (p * n * r)/100
    print('The Simple Interest is', si)
    return f'The simple Interest is {0}'.format(si)

simple(2500,5,5)
# Time complexity: O(1)


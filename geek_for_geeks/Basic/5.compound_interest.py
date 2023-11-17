# Compound Interest
# A = P(1 + R/100) t 
# Compound Interest = A – P 
# A is amount 
# P is the principal amount 
# R is the rate and 
# T is the time span

# # calculates the compound interest
# a=p*(1+(r/100))**t  # formula for calculating amount 
# ci=a-p  # compound interest = amount - principal amount


def compound_interest(p, r, t):
 
    # Calculates compound interest
    a = p* (pow((1 + r / 100), t))
    CI =a-p
    print("Compound interest is", CI)
 
 
compound_interest(10000, 10, 5)

# Time Complexity: O(1) 


# Compound Interest using for loop

def compound_interest(principal, rate, time):
    Amount = principal
    for i in range(time):
        Amount = Amount * (1 + rate/100)
    CI = Amount - principal
    print("Compound interest is", CI)

compound_interest(1200, 5.4, 2)
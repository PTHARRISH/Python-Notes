# Euclid Algorithm

def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        diff = m - n
        return gcd(max(n, diff), min(n, diff))


print(gcd(11, 2222))
# The function prints 11 because 11 is the greatest common divisor (GCD) of the numbers 11 and 2222.
# Let's break down the process:
# Initial Call: gcd(11, 2222)
# Swap Values: Since 11 < 2222, swap them. Now it's gcd(2222, 11)
# Check Remainder: 2222 % 11 is not 0, so it calculates the difference: 2222 - 11 = 2211
# Recursive Call: gcd(2211, 11)
# Check Remainder: 2211 % 11 is 0
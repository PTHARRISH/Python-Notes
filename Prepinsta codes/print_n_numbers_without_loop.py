# print_n_numbers_without_using_for_loop
def print_n_numbers(n):
    if n>0:
        print_n_numbers(n-1)
        print(n)
print_n_numbers(100)

# import numpy as np
# a=np.arange(1,100)
# print(a)

print(*range(1,100))
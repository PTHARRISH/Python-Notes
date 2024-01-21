# Itertools.permutation()
# Itertools.permutation() function falls under the Combinatoric Generators. 
# The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, 
# and Cartesian products are called combinatoric iterators

# The word “Permutation” it refers to all the possible combinations in which a set or string can be ordered or arranged. 
# Similarly here itertool.permutations() method provides us with all the possible arrangements 
# that can be there for an iterator and all elements are assumed to be unique on the basis of their position 
# and not by their value or category. 

# All these permutations are provided in lexicographical order. 
# The function itertool.permutations() takes an iterator 
# and ‘r’ (length of permutation needed) as input and 
# assumes ‘r’ as default length of iterator 
# if not mentioned and returns all possible permutations of length ‘r’ each. 

# Syntax:
# Permutations(iterator, r)

# Example:
from itertools import permutations 
name="HASH"
p=permutations(name) # it return permutation object <itertools.permutations object at 0x000001DED0B63100>
for i in list(p):
    print(i) # print each value inside the permutation object


# Example:
print ("All the permutations of the given list is:") 
print (list(permutations([1, 'Spider'],2))) 
print() 

# All the permutations of the given list is:
# [(1, 'Spider'), ('Spider', 1)]
 

print ("All the permutations of the given string is:") 
print (list(permutations('PT'))) 
print() 

# All the permutations of the given string is:
# [('P', 'T'), ('T', 'P')]


print ("All the permutations of the given container is:") 
print(list(permutations(range(3), 2)))  # 2 is r -> refers to the length or dimension 

# If r and length is mentioned here the output is
# All the permutations of the given container is (range(3), 2):
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

# If r or length is not mentioned here the output is
# All the permutations of the given container is (range(3)):
# [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


# Example:

lst=["a","b","c"]

print("\nCombination of letters: ")
for i in permutations(lst):
    print("".join(i))

# Combinations()
# The combinations() function in Python, part of the itertools module,
# is used to generate all possible combinations of a specified length from a given iterable
# (like a list, string, or tuple).
# Unlike permutations, where the order does matter,
# combinations focus only on the selection of elements, meaning the order does not matter.
# It returns an iterator producing tuples, each representing a unique combination of the input elements.


# Example:
from itertools import combinations

a = "GeEK"
# generate all combinations of length 2
for j in combinations(a, 2):
    print(j)

# ('G', 'e')
# ('G', 'E')
# ('G', 'K')
# ('e', 'E')
# ('e', 'K')
# ('E', 'K')


# Explanation:
# itertools.combinations()
# generates all unordered pairs (length = 2) from the string "GeEK".
# Each element is treated by its position and value.
# The order within each tuple doesn't matter and no duplicate combinations (like ('e', 'G')) are included.

# Syntax of Itertools.Combinations()
# itertools.combinations(iterable, r)

# Parameters:

# iterable: The input sequence (list, string, tuple, etc.) from which combinations are formed.
# r: The length of each combination to be generated.
# Returns: An iterator that produces tuples, each representing a unique combination of r elements from the iterable, in the order they appear.

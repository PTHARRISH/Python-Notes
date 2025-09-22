from itertools import permutations

s = input().split()
S, k = s[0], int(s[1])

for p in sorted(permutations(S, k)):
    print("".join(p))

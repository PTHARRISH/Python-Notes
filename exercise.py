
#1. Some Generative Art
# import sys
# import random
# chars="\|/"
# def draw(rows, columns):
#     for r in rows:
#         print(''.join(random.choice(chars) for _ in range(columns)))

# draw(10,20)

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
    


rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')



rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")

n=int(input("Enter the number: ")) # 5

print("--------------------------------------------------------")

# *****
# *****
# *****
# *****
# *****

for i in range(n):
    print("*"*n)

print("--------------------------------------------------------")

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("--------------------------------------------------------")

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()

print("--------------------------------------------------------")

# 1
# 22
# 333
# 4444
# 55555
# 666666

for i in range(n+1):
    for j in range(i):
        print(i,end="")
    print()

print("--------------------------------------------------------")

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
for i in range(n):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print() 

print("--------------------------------------------------------")

    
print("--------------------------------------------------------")
# 1
# 1 2
# 1 2 6
# 1 2 6 24
# 1 2 6 24 120

for i in range(1,n+1):
    sum=1
    for j in range(1,i+1):
        sum*=j
        print(sum,end=" ")
    print()

print("--------------------------------------------------------")
print("Pascal triangle")

# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1 
def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()

def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num
# set rows
rows = 7
print_pascal_triangle(rows)

print("--------------------------------------------------------")
print("Print number in reverse order ")

# 1
# 3 2
# 6 5 4
# 10 9 8 7
start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop



print("--------------------------------------------------------")
print("Reverse number in pattern ")
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")


print("--------------------------------------------------------")

# reverse for loop from 5 to 0
print("reverse for loop from n to 0 ")
# 1 1 1 1 1 
# 2 2 2 2
# 3 3 3
# 4 4
# 5

rows = 5
b = 0

for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

print("--------------------------------------------------------")
# x patter number

# 1    6
#  2  5
#   34
#   34
#  2  5
# 1    6

n = int(input())
for i in range(0, n+1):
    for j in range(1, n+1):
        if i == j or i + j == n+1:
            print(j,end="")
        else:
            print(" ",end='')
    print()


print("--------------------------------------------------------")

# diamond pattern

#       0
#      1 1
#     2 2 2
#    3 3 3 3
#   4 4 4 4 4
#  5 5 5 5 5 5
# 6 6 6 6 6 6 6
#  0 0 0 0 0 0
#   1 1 1 1 1
#    2 2 2 2
#     3 3 3
#      4 4
#       5


n = int(input())
# n=k+1
for i in range(0, n+1):
    for j in range(0, n - i):
        print(" ", end="")
    for j in range(0, i + 1):
        print(i, end=" ")
    print()
    # n = n - 1
# n = k+1
for i in range(0, n):
    for j in range(0, i+1):
        print(" ", end="")
    for j in range(0, n - i):
        print(i, end=" ")
    print()

print("--------------------------------------------------------")

# 2. diamond pattern
  
#       0
#      1 1
#     2 2 2
#    3 3 3 3
#   4 4 4 4 4
#  5 5 5 5 5 5
# 6 6 6 6 6 6 6
#  5 5 5 5 5 5
#   4 4 4 4 4
#    3 3 3 3
#     2 2 2
#      1 1
#       0


n = int(input())
# n=k+1
for i in range(0, n + 1):
    for j in range(0, n - i):
        print(" ", end="")
    for j in range(0, i + 1):
        print(i, end=" ")
    print()
    # n = n - 1
# n = k+1
for i in range(n - 1, -1, -1):
    for j in range(0, n - i):
        print(" ", end="")
    for j in range(0, i + 1):
        print(i, end=" ")
    print()

print("--------------------------------------------------------")

#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("--------------------------------------------------------")


#         5 4 3 2 1
#       5 4 3 2 1
#     5 4 3 2 1
#   5 4 3 2 1
# 5 4 3 2 1

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    
    for j in range(n,0,-1):
        print(j,end=" ")
    
    print()



print("--------------------------------------------------------")

# x pattern name

# 1   5
#  2 4
#   3
#  2 4
# 1   5

n = input()
for i in range(0, len(n)):
    for j in range(0, len(n)):
        if i == j or i + j == len(n)-1:
            print(n[j],end="")
        else:
            print(" ",end='')
    print()

print("--------------------------------------------------------")


# triangle pattern

#      0
#     1 1
#    2 2 2
#   3 3 3 3
#  4 4 4 4 4
# 5 5 5 5 5 5
#  0 0 0 0 0
#   1 1 1 1
#    2 2 2
#     3 3
#      4

n = int(input())
for i in range(0, n):
    for j in range(0, n + 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print(i, end=" ")
    print()
    n = n - 1


print("--------------------------------------------------------")

# 0 0 0 0 0 0
#  1 1 1 1 1
#   2 2 2 2
#    3 3 3
#     4 4
#      5

# reverse triangle
n = 6
for i in range(0, n):
    for j in range(0, i):
        print(" ", end="")
    for j in range(0, n - i):
        print(i, end=" ")
    print()



print("--------------------------------------------------------")

#1. Some Generative Art
# import sys
# import random
# chars="\|/"
# def draw(rows, columns):
#     for r in rows:
#         print(''.join(random.choice(chars) for _ in range(columns)))

# draw(10,20)
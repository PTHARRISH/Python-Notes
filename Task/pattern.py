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


# 1    6
#  2  5
#   34
#   34
#  2  5
# 1    6

# x patter number
n = int(input())
for i in range(0, n+1):
    for j in range(1, n+1):
        if i == j or i + j == n+1:
            print(j,end="")
        else:
            print(" ",end='')
    print()



print("--------------------------------------------------------")
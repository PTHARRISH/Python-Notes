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

for i in range(n+1):
    for j in range(i):
        print(i,end="")
    print()

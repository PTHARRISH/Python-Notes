
# rows = 5
# i = 1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print((i * 2 - 1), end=" ")
#         j = j + 1
#     i = i + 1
#     print('')
#

# print('\n') 
# x=input("enter symbol: ")
# n= int(input("enter a number: "))
# for i in range(n):
#     print(x*n)
    

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# print("Row i value print it")
# a=int(input("Enter number: "))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n=int(input("enter: "))
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# a,b=0,1
# for i in range(n):
#     for j in range(i+1):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
#     print()



# a=0
# b=0
# for i in range(n):
#     for j in range(i+1): 
#             c=a+b
#             if b==0 or a==0:
#                 b=1
#             a=b
#             b=c
#             print(c,end=" ")
#     print()

# a = 0
# b = 1
# for i in range(n):
#     for j in range(i+1): 
#             print(a, end=" ")
#             c = a + b
#             a = b
#             b = c
#     print()

n = int(input())
# n=k+1
a=0
b=1
for i in range(0, n+1):
    for j in range(0, n - i):
        print(" ", end="")
    for j in range(0, i + 1):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()
    # n = n - 1
# n = k+1
for i in range(0, n):
    for j in range(0, i+1):
        print(" ", end="")
    for j in range(0, n - i):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()

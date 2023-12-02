def transposed(arr):
    transposed=[]
    n=len(arr)
    m=len(arr[0])
    for j in range(m):
        a=[]
        for i in range(n):
            a.append(arr[i][j])
        transposed.append(a)
    return transposed

# def reverse_row(arr):
#     for i in range(len(arr)):
#         arr[i]=arr[i][::-1]
#     return arr

# def rotate(arr):
#     n=len(arr)
#     m=len(arr[0])
#     rotate=[]
#     for j in range(m):
#         a=[]
#         for i in range(n-1,-1,-1):
#             a.append(arr[i][j])
#         rotate.append(a)
#     return rotate



# n=int(input())
# m=int(input())
# arr=[[int(input()) for i in range(m)] for j in range(n)]
# # arr=list(map(int,input().split(' ')))
# print(arr)
# print(rotate(arr))
# # print(reverse_row(arr))
# print(transposed(arr))

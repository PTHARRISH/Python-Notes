# Bubble Sort
def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            print(i,j)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
    return arr

# arr=list(map(int,input("enter the numbers: ").split(",")))
# print(bubble(arr))
# i j
# 0 0 -> j[0]>j[1]=[1,3,0,2,5,6,4]
# 0 1 -> j[1]>j[2]=[1,3>0,2,5,6,4] True
# [1, 0, 3, 2, 5, 6, 4]
# 0 2 -> j[2]>j[3]=[1, 0, 3> 2, 5, 6, 4] True
# [1, 0, 2, 3, 5, 6, 4]
# 0 3 -> j[3]>j[4]=[1, 0, 2, 3>5, 6, 4]
# 0 4 -> j[4]>j[5]=[1, 0, 2, 3, 5>6, 4]
# 0 5 -> j[5]>j[6]=[1, 0, 2, 3, 5, 6>4] True
# [1, 0, 2, 3, 5, 4, 6]
# 1 0 -> j[0]>j[1]=[1>0, 2, 3, 5, 4, 6] True
# [0, 1, 2, 3, 5, 4, 6]
# 1 1
# 1 2
# 1 3
# 1 4
# [0, 1, 2, 3, 4, 5, 6]
# 2 0
# 2 1
# 2 2
# 2 3
# 3 0
# 3 1
# 3 2
# 4 0
# 4 1
# 5 0
# [0, 1, 2, 3, 4, 5, 6]



def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=True
        for j in range(n-i-1):
            print(i,j)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if not swapped:
            break
    return arr
arr=list(map(int,input("enter the numbers: ").split(",")))
print(bubble_sort(arr))

# Bubble Sort

# Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them 
# until they are in the intended order.

# Starting from the first index, compare the first and the second elements
# If the first element is greater than the second element, they are swapped.
# Now, compare the second and the third elements. Swap them if they are not in order.
# The above process goes on until the last element.


def bubble(arr):
    n=len(arr)# 7
    for i in range(n): # 0,7
        for j in range(n-i-1): # 7-0-1 (0,6)
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


# Optimized Bubble Sort Algorithm
# In the above algorithm, all the comparisons are made even if the array is already sorted.
# This increases the execution time.
# To solve this, we can introduce an extra variable swapped. 
# The value of swapped is set true if there occurs swapping of elements. Otherwise, it is set false.
# After an iteration, if there is no swapping, the value of swapped will be false.
# 


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


# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 1 0
# 1 1
# 1 2
# 1 3
# 2 0
# 2 1
# 2 2
# 3 0
# 3 1
# 4 0
# [0, 1, 2, 3, 5, 8]

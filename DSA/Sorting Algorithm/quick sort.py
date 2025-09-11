# Quick Sort
# Approach 1:
# def partition(data,l,r):
#     pivot=data[r]
#     i=l-1#0
#     for j in range(l,r):
#         if data[j]<=pivot:
#             i=i+1
#             (data[i],data[j])=(data[j],data[i])
#     (data[i+1],data[r])=(data[r],data[i+1])
#     return i+1

# def quickSort(data,l,r):
#     if l<r:
#         pi=partition(data,l,r)
#         quickSort(data,l,pi-1)
#         quickSort(data,pi+1,r)

# data=[1,7,4,1,10,9,-2]
# print("Unsorted Array")
# print(data)
# r=len(data)-1
# print(r)
# quickSort(data,0,r)
# print('Sorted Array in Ascending Order:')
# print(data)

# Approach 2: Quicksort using list comprehension

# def quicksort(arr):
# 	if len(arr) <= 1:
# 		return arr
# 	else:
# 		pivot = arr[0]
# 		left = [x for x in arr[1:] if x < pivot]
# 		right = [x for x in arr[1:] if x >= pivot]
# 		return quicksort(left) + [pivot] + quicksort(right)

# # Example usage
# arr = [1, 7, 4, 1, 10, 9, -2]
# sorted_arr = quicksort(arr)
# print("Sorted Array in Ascending Order:")
# print(sorted_arr)


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr = [700, 200, 400, 100, 90]
print(quick_sort(arr))

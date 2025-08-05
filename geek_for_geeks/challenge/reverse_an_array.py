# 3.Reverse An Array
# Two Pointer Approach (best approach)
def reverseArray(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr


# T.C = O(n)
# S.C = O(1)


# Naive method
# def reverseArray(arr):
#     temp = []
#     n = len(arr)
#     for i in range(n):
#         temp.append(arr[n - 1 - i])
#     # for i in range(len(arr) - 1, -1, -1):
#     #     temp.append(arr[i])
#     return temp


# T.C = O(n)
# S.C = O(n)

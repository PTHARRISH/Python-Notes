# Best Approach (3rd method)
def pushZerosToEnd(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr


# T.C = O(n)
# S.C = O(1)


# def pushZerosToEnd(arr):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         if arr[i] != 0:
#             arr[count] = arr[i]
#             count += 1
#     while count < n:
#         arr[count] = 0
#         count += 1
#     return arr


# T.C = O(2n)
# S.C = O(1)

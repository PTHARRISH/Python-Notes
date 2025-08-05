# 1.Second Largest 
# Using One Iteration(Best method)
def getSecondLargest(arr):
    n = len(arr)
    first = second = float("-inf")
    if n < 2:
        return -1
    else:
        for i in arr:
            if i > first:
                second = first
                first = i
            elif i > second and i != first:
                second = i
        if second == float("-inf"):
            return -1
        return second


# T.C = O(n)
# S.C = O(1)


# Using Two iteration
# def getSecondLargest(arr):
#     n = len(arr)
#     first = second = float("-inf")
#     if n < 2:
#         return -1
#     for i in range(len(arr)):
#         if arr[i] > first:
#             first = arr[i]
#     for i in range(len(arr)):
#         if arr[i] != first and second < first and arr[i] > second:
#             second = arr[i]

#     if second == float("-inf"):
#         return -1
#     return second


# T.C = O(2n)
# S.C = O(1)


# Using sorted()
# def getSecondLargest(arr):
#     n = len(arr)
#     data = sorted(arr)
#     first = second = float("-inf")
#     if n < 2:
#         return -1
#     else:
#         first = max(arr)
#     for i in range(len(data) - 1, 0, -1):
#         if data[i] != first:
#             second = data[i]
#             break
#     if second == float("-inf"):
#         return -1
#     return second


# T.C = O(n log n)
# S.C = O(1)

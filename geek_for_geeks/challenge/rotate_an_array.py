# 4.rotate an array
# Reversal Algorithm(best approach)
def rotateArr(arr, d):
    n = len(arr)
    d %= n

    def reversal(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

    reversal(arr, 0, d - 1)
    reversal(arr, d, n - 1)
    reversal(arr, 0, n - 1)
    return arr


# T.C = O(n)
# S.C = O(1)


# def rotateArr(arr, d):
#     n = len(arr)
#     d = d % n
#     return arr[d:] + arr[:d]


# T.C = O(n)
# S.C = O(n)


# def rotateArr(arr, d):
#     n = len(arr)
#     temp = []
#     for i in range(d, n):
#         temp.append(arr[i])
#     for j in range(0, d):
#         temp.append(arr[j])
#     return temp


# T.C = O(n)
# S.C = O(n)


# def rotateArr(arr, d):
#     n = len(arr)
#     first = 0
#     for i in range(d):
#         first = arr[0]
#         for j in range(n - 1):
#             arr[j] = arr[j + 1]
#         arr[n - 1] = first
#     return arr


# T.C = O(d*n)
# S.C = O(1)


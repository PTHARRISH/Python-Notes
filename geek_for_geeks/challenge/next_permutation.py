def nextPermutation(arr):
    n = len(arr)
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    if pivot == -1:
        arr.reverse()
        return
    for i in range(n - 1, pivot, -1):
        if arr[pivot] < arr[i]:
            arr[pivot], arr[i] = arr[i], arr[pivot]
            break
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# print(nextPermutation([1, 2, 4, 5, 6, 0]))

# T.C = O(n)
# S.C = O(1)

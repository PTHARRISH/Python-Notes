# 6.Majority Element - More Than n/3
def findMajority(arr):
    data = {}
    n = len(arr)
    t = n // 3
    majority = []
    for i in arr:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    for key in data:
        if data[key] > t:
            majority.append(key)
    return sorted(majority)


# T.C = O(n)
# S.C = O(n)

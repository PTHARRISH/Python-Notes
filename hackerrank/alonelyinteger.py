def lonelyinteger(a):
    b = sorted(a)
    if len(b) == 1:
        return b[0]
    else:
        for i in range(len(b)):
            count = 0
            for j in range(len(b)):
                if b[i] == b[j]:
                    count += 1
            if count == 1:
                return b[i]


def lonelyinteger(a):
    b = sorted(a)
    data = {}
    if len(b) == 1:
        return b[0]
    else:
        for i in b:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        for key, value in data.items():
            if value == 1:
                return key


a = list(map(int, input().split()))
print(lonelyinteger(a))

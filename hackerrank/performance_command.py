    
N = int(input())
i = 1
data = []
while i <= 12:
    a = input()
    d = a.split()
    if d[0] == "insert":
        data.insert(int(d[1]), int(d[2]))
    elif d[0] == "remove":
        data.remove(int(d[1]))
    elif d[0] == "append":
        data.append(int(d[1]))
    elif d[0] == "sort":
        data.sort()
    elif d[0] == "pop":
        data.pop()
    elif d[0] == "reverse":
        data.reverse()
    elif d[0] == "print":
        print(data)
    i += 1
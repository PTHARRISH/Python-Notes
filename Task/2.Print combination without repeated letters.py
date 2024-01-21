# Task 2: Print combination without repeated letters

a=["a","b","c"]

for i in a:
    print(i)

for i in a:
    for j in a:
        if i==j:
            continue
        else:
            print(i+j)

for i in a:
    for j in a:
        for k in a:
            if i==j or j==k or k==i:
                continue
            else:
                print(i+j+k)


lst=[]
for i in range(len(a)):
    lst.append(a[i])
    for j in range(len(a)):
        if i==j:
            continue
        lst.append(a[i]+a[j])
        for k in range(len(a)):
            if i==j or j==k or k==i:
                continue
            lst.append(a[i]+a[j]+a[k])
print(lst)

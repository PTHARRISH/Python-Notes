def vowels(n):
    result=""
    list1=["A","E","I","O","U","a","e","i","o","u"]
    for i in n:
        if i in list1:
            if n[n.index(i)+1]==i:
                result+=i
            else:
                pass
        else:
            result+=i
    print(result)


n=input()
vowels(n)
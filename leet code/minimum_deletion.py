import collections
def mindeletion(s):
    deletion=0
    freq=set()
    charco=collections.Counter(s)
    for chars,counts in charco.items():
        while counts>0 and counts in freq:
            counts-=1
            deletion+=1
        freq.add(counts)
    return deletion

a=input('enter: ')
result=mindeletion(a)
print(result)


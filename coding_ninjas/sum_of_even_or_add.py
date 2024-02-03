sum_of=input()
odd=0
even=0
for i in sum_of:
    a=int(i)
    if a%2==0 or a==0:
        even+=a
    else:
        odd+=a

print(even,odd)

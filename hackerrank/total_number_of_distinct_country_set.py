def total_number_of_distinct_country ():
    n=int(input())
    s=set()
    for i in range(n):
        name=input()
        s.add(name)
    print(len(s))

total_number_of_distinct_country()
if __name__ == '__main__':
    x = int(input('enter the x : '))
    y = int(input('enter the y : '))
    z = int(input('enter the z : '))
    n = int(input('enter the n number: '))
    ijk=[]
    # abc=[]
    list1=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k!=n:
                    ijk=[i,j,k]
                    list1.append(ijk)
    print(list1)

    # using list comprehension
    # list2=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n ]
    # print(list2)
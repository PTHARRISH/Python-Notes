# Print all Prime numbers in an Interval 
# using for loop
def prime_intervel(x,y):
    lst=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    break
            else:
                lst.append(i)
    return(lst)
x=int(input('Enter starting value: '))
y=int(input('Enter ending value: '))
list1=prime_intervel(x,y)
if len(list1)==0:
    print(f'There is no prime number between {x} and {y}'.format(x,y))
else:
    print(f'The prime number between {x} and {y} is'.format(x,y),list1)

# method 1
print('Numbers\t\tSquares')
print('1 \t\t '+str(1*1))
print('2 \t\t '+str(2*2))
print('3 \t\t '+str(3*3))
print('4 \t\t '+str(4*4))


# method 2
def number_squares(n):
    print(str(n)+' \t\t '+str(n*n))

start_num,end_num = input('enter the starting and ending number:').split(' ')
if start_num<=end_num:
    for n in range(int(start_num),int(end_num)+1):
        number_squares(n)
else:
    print('enter the proper range')


# method 3 : optimized 

def number_squares(start_num,end_num):
    if start_num>end_num:
        print('Invalid Range: Starting number must be less than or equal to the ending number.')
        return
    for n in range(start_num,end_num+1):
        print(f"{n}\t\t{n*n}")
        
try:
    start_num,end_num=map(int,input('Enter the starring and ending range with single space:').split(' '))
    print('Numbers\t\tSquares')
    number_squares(start_num,end_num)
except ValueError:
    print("Invalid input! Please enter two integers separated by a space.")
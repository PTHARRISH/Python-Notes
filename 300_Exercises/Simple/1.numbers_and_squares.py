# 1.Python to find the range of numbers that are squares within a specified limit
# method 1
print('Numbers\t\tSquares')
print('1 \t\t '+str(1*1))
print('2 \t\t '+str(2*2))
print('3 \t\t '+str(3*3))
print('4 \t\t '+str(4*4))

# output:
# Numbers         Squares
# 1                1
# 2                4
# 3                9
# 4                16

# method 2:
def number_squares(start_num,end_num):
    if start_num>end_num:
        print('Invalid Range: Starting number must be less than or equal to the ending number.')
        return
    for n in range(start_num,end_num+1):
        print(f"{n}\t\t{n*n}")
        
try:
    start_num,end_num=map(int,input('Enter the starting and ending range with single space:').split(' '))
    print('Numbers\t\tSquares')
    number_squares(start_num,end_num)
except ValueError:
    print("Invalid input! Please enter two integers separated by a space.")


# output:
# Enter the starting and ending range with single space:10 20
# Numbers         Squares
# 10              100
# 11              121
# 12              144
# 13              169
# 14              196
# 15              225
# 16              256
# 17              289
# 18              324
# 19              361
# 20              400

# Assignment 1:
# In Python to find the range of numbers that are both squares and cubes within a specified limit 
def number_square_cubes(start_num,end_num):
    if start_num>end_num:
        print('Invalid Range: Starting number must be less than or equal to the ending number.')
        return
    for n in range(start_num,end_num+1):
        print(f"{n}\t\t{n*n}\t\t{n*n*n}")

try:
    start_num,end_num=map(int,input('Enter the starting and ending range with single space:').split(' '))
    print('Numbers\t\tSquares\t\tCubes')
    number_square_cubes(start_num,end_num)
except ValueError:
    print("Invalid input! Please enter two integers separated by a space.")


# output:
# Enter the starring and ending range with single space:5 15
# Numbers         Squares         Cubes
# 5               25              125
# 6               36              216
# 7               49              343
# 8               64              512
# 9               81              729
# 10              100             1000
# 11              121             1331
# 12              144             1728
# 13              169             2197
# 14              196             2744
# 15              225             3375

# Time Complexity

# The main time complexity comes from the loop, which iterates over the numbers in the range [start_num, end_num]. 
# As mentioned above, the loop runs N=end_num−start_num+1
# N=end_num−start_num+1 times, and each iteration involves constant-time operations.

# Thus, the time complexity of the code is:
# O(N)whereN=end_num−start_num+1

# If the size of the input range increases, the number of iterations increases linearly, 
# so the time complexity is O(N).

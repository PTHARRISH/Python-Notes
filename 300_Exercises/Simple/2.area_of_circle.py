# 2.Calculate the Area of circle
# Method 1:
def area_of_circle(n):
    print(f'Area of the circle {n} is {3.14*n*n}')

n = float(input('Enter the area of circle N value : '))
area_of_circle(n)

# output:
# Enter the area of circle N value : 10
# Area of the circle 10.0 is 314.0

# method 2:
import math

def area_of_circe(n):
    print(f'Area of the circle {n} is {math.pi*n**2}')

n = float(input('Enter the area of circle N value : '))
area_of_circe(n)

# output:
# Enter the area of circle N value : 20
# Area of the circle 20.0 is 1256.6370614359173

# Assignment 2:
# Calculate the Area of the Rectangle
def area_of_rectangle(l,b):
    print(f'Area of rectangle with length {l} and breadth {b} is {l * b}')

l,b = map(float, input('Enter the Length and Breadth of the rectangle with single space: ').split(' '))
area_of_rectangle(l,b)

# output:
# Enter the Length and Breadth of the rectangle with single space: 10 20
# Area of rectangle with length 10.0 and breadth 20.0 is 200.0

# Time Complexity:
# The input handling (map(float, input().split())) takes constant time to process two values, so it's O(1).
# The function call and the multiplication inside it also take constant time, so that part is O(1).

# Thus, the overall time complexity of the code is O(1), 
# meaning the runtime does not depend on the size of the input and remains constant.
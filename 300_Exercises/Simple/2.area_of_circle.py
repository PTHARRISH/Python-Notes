# 2.Calculate the Area of circle
# Method 1:
def area_of_circle(n):
    print(f'Area of the circle {n} is {3.14*n*n}')

n = float(input('Enter the n Number: '))
area_of_circle(n)


# method 2:
import math

def area_of_circe(n):
    print(f'Area of the circle {n} is {math.pi*n**2}')

n = float(input('Enter the n Number: '))
area_of_circe(n)

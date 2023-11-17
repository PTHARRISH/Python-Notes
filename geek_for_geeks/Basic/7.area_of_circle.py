# Area of a circle
# formula = pi*(r*r)
def findArea(r):
    PI = 3.142
    return PI * (r*r)
 
print("Area is %.6f" % findArea(5))
# Time Complexity: O(1)


# using inbuild library
import math
def area(r):
  area = math.pi* pow(r,2)
  return print('Area of circle is:' ,area)
area(4)
# Time Complexity: O(1)
# method Overloading
# Method overloading is a feature that allows a class to have more than one method with the same name, 
# but different parameters.
# In Python, method overloading is not supported directly, 
# but we can achieve it using the multipledispatch library.
# To use the multipledispatch library, you need to install it first. You can do this using pip:
# pip install multipledispatch
# After installing the library, you can use it to create overloaded methods in your class.
# Here is an example of method overloading using the multipledispatch library:
# pip install multipledispatch


from multipledispatch import dispatch

# passing one parameter

class pro:
    @dispatch(int, int)
    def product(first, second):
        result = first*second
        print(result)

    # passing two parameters


    @dispatch(int, int, int)
    def product(first, second, third):
        result = first * second * third
        print(result)

    # you can also pass data type of any value as per requirement


    @dispatch(float, float, float)
    def product(first, second, third):
        result = first * second * third
        print(result)

obj=pro()
# calling product method with 2 arguments
obj.product(2, 3) # this will give output of 6

# calling product method with 3 arguments but all int
obj.product(2, 3, 2) # this will give output of 12

# calling product method with 3 arguments but all float
obj.product(2.2, 3.4, 2.3) # this will give output of 17.985999999999997


class table:
    @dispatch(int)
    def table(self, n):
        for i in range(1, 11):
            print(f"{n} * {i} = {n * i}")

    @dispatch(int, int)
    def table(self, n, m):
        for i in range(1, m + 1):
            print(f"{n} * {i} = {n * i}")


obj = table()
# calling table method with 1 argument
obj.table(2)  # this will give output of 2 * 1 = 2, 2 * 2 = 4, ..., 2 * 10 = 20
# calling table method with 2 arguments
obj.table(2, 5)  # this will give output of 2 * 1 = 2, 2 * 2 = 4, ..., 2 * 5 = 10
# calling table method with 3 arguments
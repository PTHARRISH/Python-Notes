# Stack
# Stack is an ordered collection of items where the addition of new items and removal items
# always taken place at same end.
# So the end is called as top.
# And the opposite end is known as base.
# Stack stored items in Last In First Out (LIFO) or First In Last Out (FILO)
# Stack stores the data element in similiar fashion ,
# as the bunch of plates are kept one above the another in a kitchen.

# If you add an object in a stack it will store in a base and second store top of the 1'st object
# like that way it will stores 
# If you want to remove the top first object it is called (LIFO)or(FILO)

# Stack implementation in python

print("_______________________________________________________")
# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))



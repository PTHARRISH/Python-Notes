# Single linkedlist
class Node:
    def __init__(self, data):
        self.data = data  # create data or node
        self.next = None  # default next is none


class Sll:
    def __init__(self):
        self.head = None  # Head node is starting node

    def traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next
            print()

    def insert_beginning(self, data):
        print("Insert at the beginning:")
        nb = Node(data)
        nb.next = self.head
        self.head = nb


n1 = Node(5)  # create a data=5 and pass value in Node class
sll = Sll()  # create a object of sll
sll.head = n1  # now assign a n1 object to sll.head variable now sll.head=5
n2 = Node(10)  # and create another data=10 node and pass value in Node class
n1.next = n2  # now connect the two nodes
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4
sll.traversal()
sll.insert_beginning(1)
sll.traversal()


# Output:
# 5 10 15 20

#
# First we pass the 5 data in Node class. n1 have n1.data=5
# Then we create the object for Sll default constructor will execute then it sll.head = none.
# Then we assign the sll.head = n1 which is nothing but n1 so sll.head = n1
# Now we create another data for n2 which have Node(10) now n2.data=10 wil assign
# now we need to connect nodes n1.next = none is default but we are modifing now n1.next = n2
# same way we are mapping untill last node
# we finally mapped how to print it.
# For that reason in Sll class we create function called tranversal()
# sll.traversal we are calling at last now it will check sll.head is none or not
# sll.head is n1 so it will go to else part there we are printing a = self.head we are keeping
# then we are checking in while a is not none inside while print the a.data
# then after we are reassigning a = a.next which is n2 again it went to while its not none
# then n2.data will print then n2.next = n3 now a = n3
# it will repeat untill last node.

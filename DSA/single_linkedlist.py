# Single linkedlist
class Node:
    def __init__(self,data):
        self.data=data # create data or node
        self.next=None # default next is none

class Sll:
    def __init__(self):
        self.head=None # Head node is starting node
    
    def tranversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next

n1=Node(5) # create a data=5 and pass value in Node class 
sll=Sll() # create a object of sll 
sll.head=n1 # now assign a n1 object to sll.head variable now sll.head=5
n2=Node(10) # and create another data=10 node and pass value in Node class 
n1.next=n2 # now connect the two nodes
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4
sll.tranversal()
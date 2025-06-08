from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=l1
        count=""
        while head!=None:
            count+=str(head.val)
            head=head.next
        
        count=int(count[::-1])

        head=l2
        count1=""
        while head!=None:
            count1+=str(head.val)
            head=head.next
        
        count1=int(count1[::-1])
        ans=count+count1
        list1=None
        for i in str(ans)[::-1]:
            if list1==None:
                list1=ListNode(int(i))
                head=list1
            else:
                n1=ListNode(int(i))
                list1.next=n1
                list1=n1
        return head
print(Solution.addTwoNumbers(l1=[2,4,7],l2=[1,3,5]))
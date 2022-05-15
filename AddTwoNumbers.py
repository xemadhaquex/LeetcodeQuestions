# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        liste=ListNode()
        node=liste
        carry=0
        
        while l1 or l2:
            if l1.next == None and l2.next!=None:
                l1.next=ListNode()
            if l2.next ==None and l1.next !=None:
                l2.next=ListNode()
            if carry ==1:
                newval = l1.val+l2.val+1
                carry=0
            else:
                newval = l1.val+l2.val
            
            if newval >9:
                carry=1
            newval=newval%10
            node.next = ListNode(newval)
            
            node=node.next
            l1=l1.next
            l2=l2.next
        
        if carry==1:
            node.next=ListNode(1)
        
        return liste.next

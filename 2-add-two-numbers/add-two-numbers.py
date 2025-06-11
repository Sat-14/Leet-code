# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        

        while l1:
         
         list1.append(l1.val)
         l1=l1.next
        while l2:
           
            list2.append(l2.val)
            l2=l2.next
            
        a=int(("".join(map(str,list1[::-1]))))
        b=int(("".join(map(str,list2[::-1]))))
        c=str(a+b)
        list3 = [int(digit) for digit in str(c[::-1])] 
        dh=ListNode(0)
        ch=dh
        for digits in list3:
            ch.next=ListNode(digits)
            ch=ch.next
        result=dh.next
        return result    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self,curr,prev):
        if curr == None:
            return prev
        temp = curr.next
        curr.next = prev
        return self.helper(temp,curr)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head,None)
        
        
#---------------------------------------ITERATIVE---------------------------------------------------------
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         curr = head
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dmnode=ListNode(0)
        dmnode.next=head
        
        curr = dmnode
        while curr.next!=None:
            if curr.next.val == val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dmnode.next
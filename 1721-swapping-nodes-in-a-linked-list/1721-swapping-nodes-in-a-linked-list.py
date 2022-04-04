# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        f_node = last_node = head
        temp = f_node.next
        
        for i in range(k-1):
            f_node = f_node.next # kth value from the first
            temp = temp.next
            
        while temp:
            temp = temp.next
            last_node = last_node.next # kth value from the last
                 
        last_node.val,  f_node.val = f_node.val, last_node.val #Swap the value
        
        
        return head
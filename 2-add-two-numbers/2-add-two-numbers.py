# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next = l1)
        prev = None
        carry = 0
        
        while l1 and l2:
            prev_l1 = l1.val
            l1.val = (carry + l1.val + l2.val) % 10
            carry = (carry + prev_l1 + l2.val) // 10
            prev = l1
            l1, l2 = l1.next, l2.next
        
        def helper_add_longer_number(node):
            nonlocal carry
            nonlocal prev
            prev.next = node
            while node:
                prev_node = node.val
                node.val = (carry + node.val) % 10
                carry = (carry + prev_node) // 10
                prev = node
                node = node.next
                
        if l1:
            helper_add_longer_number(l1)
        elif l2:
            helper_add_longer_number(l2)
        
        if carry:
            prev.next = ListNode(val = carry, next = None)
        
        return dummy_head.next
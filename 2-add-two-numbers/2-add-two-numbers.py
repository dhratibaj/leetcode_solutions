# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        dummy = head
        if not l1: return l2
        if not l2: return l1
        carry = 0
        while(l1 or l2):
            firstval = l1.val if l1 else 0
            secondval = l2.val if l2 else 0
            total = firstval + secondval + carry
            carry = total//10
            total = total%10
            newnode = ListNode(total)
            dummy.next = newnode
            dummy = dummy.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry: dummy.next = ListNode(1)
        return head.next
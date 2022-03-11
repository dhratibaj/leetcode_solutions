# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        lenght = 1
        while cur.next:
            cur = cur.next
            lenght += 1
        k %= lenght
        if k == 0:
            return head
        cur.next = head
        for _ in range(lenght - k):
            cur = cur.next
        rotate = cur.next
        cur.next = None
        return rotate
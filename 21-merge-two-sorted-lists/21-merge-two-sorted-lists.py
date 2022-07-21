# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None: return list2
        if list2==None: return list1
        if list1.val<=list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2


#-------------------------------------ITERATIVE------------------------------------------------------------------
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 == None: return list2
#         if list2 == None: return list1
#         dummy = ListNode(-101)
#         head = dummy
#         while(list1!=None and list2!=None):
#             if(list1.val<list2.val):
#                 newnode = ListNode(list1.val)
#                 dummy.next = newnode
#                 list1 = list1.next
#             else:
#                 newnode = ListNode(list2.val)
#                 dummy.next = newnode
#                 list2 = list2.next
#             dummy = dummy.next
#         if list1!=None: dummy.next = list1
#         if list2!=None: dummy.next = list2
#         return head.next
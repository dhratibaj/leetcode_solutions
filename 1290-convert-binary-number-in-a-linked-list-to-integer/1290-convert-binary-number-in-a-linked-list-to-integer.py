# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def BinToDec(self,s):
        n = len(s)
        i,j,summ = 0,n-1,0
        while(i<n):
            if(s[i]=='1'):
                summ += 2**j
            i += 1
            j -= 1
        return summ
    
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        while(head):
            s += str(head.val)
            head = head.next;
        return self.BinToDec(s)
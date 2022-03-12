"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic, itr = {}, head                                   # dic: to store each original node pointing to its copy node, itr: iterator to travese the original list
        copy_head = prev = Node(-1)                           # copy_head: head of copy List (not exactly head, but head will be at next to it), prev: this will point to previous node of Copy list, used for linking the next
        
        while itr:                                            # traverse the Original list and make the copy, we will leave the random to None as of now
            prev.next = prev = dic[itr] = Node(x = itr.val)   # make a New node with original value, link the prev.next to new node, then update the prev pointer to this new Node
            itr = itr.next                                    # update the itr to next, so we can move to the next node of original list

        copy_itr, itr = copy_head.next, head                  # copy_itr: iterator to traverse the copy list, itr: to traverse the original list
        while itr:                                            # since both are of same length, we can take while itr or while copy_itr as well
            if itr.random: copy_itr.random = dic[itr.random]  # if original has random pointer(ie not None) then update the random of copy node. Every original node is pointing to copy node in our dictionary, we will get the copy Node.
            itr, copy_itr  = itr.next, copy_itr.next          # update both iterator to its next in order to move further.
        return copy_head.next 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res,q = [],[]
        if not root: return res
        q.append(root)
        while q:
            n = len(q)
            level = []
            while(n>0):
                curr = q[0]
                q.pop(0)
                level.append(curr.val)
                n -= 1
                for i in curr.children:
                    q.append(i)
            res.append(list(level))
        return res
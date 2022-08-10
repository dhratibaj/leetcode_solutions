"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if(not root): return 0
        ans = 0
        for i in range(len(root.children)):
            temp = self.maxDepth(root.children[i])
            ans = max(ans,temp)
        return ans + 1
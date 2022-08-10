"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def Pre(self,root,ans):
        if(not root): return 
        ans.append(root.val)
        for i in range(len(root.children)):
            self.Pre(root.children[i],ans)
        return
    
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.Pre(root,ans)
        return ans
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def post(self,root,ans):
        if(not root): return 
        for i in range(len(root.children)):
            self.post(root.children[i],ans)
        ans.append(root.val)
        return
    
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.post(root,ans)
        return ans
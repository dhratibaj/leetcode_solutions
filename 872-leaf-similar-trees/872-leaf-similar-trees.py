# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,root,l):
        if(not root): return
        if(not root.left and not root.right): l.append(root.val)
        if(root.left): self.traversal(root.left,l)
        if(root.right): self.traversal(root.right,l)
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a,b=[],[]
        self.traversal(root1,a)
        self.traversal(root2,b)
        return a==b
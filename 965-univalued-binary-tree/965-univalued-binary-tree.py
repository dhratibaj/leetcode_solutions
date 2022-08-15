# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self,root,val):
        if not root: return True
        if(root.val!=val): return False
        return self.isSame(root.left,val) and self.isSame(root.right,val)
    
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.isSame(root,root.val)
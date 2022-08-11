# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftLeaf(self,root,leaf):
        if not root: return 0
        if not root.left and not root.right and leaf:
            return root.val
        ls = self.leftLeaf(root.left,True)
        rs = self.leftLeaf(root.right,False)
        return ls+rs
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leftLeaf(root,False)
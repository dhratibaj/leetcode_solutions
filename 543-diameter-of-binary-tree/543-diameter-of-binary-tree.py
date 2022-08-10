# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dia = 0
    def height(self,root):
        if(not root): return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        self.dia = max(self.dia,lh+rh)
        return 1+max(lh,rh)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.dia
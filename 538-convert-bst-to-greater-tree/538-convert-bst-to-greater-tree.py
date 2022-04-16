# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        _sum = self.convert(root, 0)
        return root
        
    def convert(self, root, _sum):
        if root.right:
            _sum = self.convert(root.right, _sum)

        _sum += root.val
        root.val = _sum
        
        if root.left:
            _sum = self.convert(root.left, _sum)  
        return _sum
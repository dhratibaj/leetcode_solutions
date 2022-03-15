# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPaths(self, root, actualValue):
        if not root:
            return False
        actualValue-=root.val
        if not root.left and not root.right:
            if actualValue == 0:
                return True
        return self.findPaths(root.left, actualValue) or self.findPaths(root.right, actualValue)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.findPaths(root, targetSum)
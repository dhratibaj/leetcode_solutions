# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root, res):
        if root == None: return 0
        res = (2 * res) + root.val
        if root.left == None and root.right == None: return res
        return self.solve(root.left, res) + self.solve(root.right, res)
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.solve(root, 0)
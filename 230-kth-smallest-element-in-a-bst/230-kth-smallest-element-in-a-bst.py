# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = -1
        
        # Do an in-order traversal of the tree.
        def recur(node: TreeNode):
            nonlocal count, result
            if node.left and result < 0:
                recur(node.left)
            count += 1
            if count == k:
                result = node.val
            if node.right and result < 0:
                recur(node.right)
                
        recur(root)
        return result
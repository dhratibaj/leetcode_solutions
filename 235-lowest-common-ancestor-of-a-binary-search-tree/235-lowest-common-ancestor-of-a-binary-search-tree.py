# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val and root.right:
            root = root.right
            return self.lowestCommonAncestor(root, p, q)


        if p.val < root.val and q.val < root.val and root.left:
            root = root.left                
            return self.lowestCommonAncestor(root, p, q)

        return TreeNode(root.val)
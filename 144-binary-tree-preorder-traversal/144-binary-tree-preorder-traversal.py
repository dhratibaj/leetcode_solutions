# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        while curr:
            res.append(curr.val)
            if not curr.left:
                curr = curr.right
            else:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr = curr.left
        return res
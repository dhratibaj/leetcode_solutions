# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def path(self,root,curr):
        if not root: return
        if not root.left and not root.right:
            curr += str(root.val)
            self.res.append(curr)
            return
        curr += str(root.val) + "->"
        if(root.left): self.path(root.left,curr)
        if(root.right): self.path(root.right,curr)
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.path(root,"")
        return self.res
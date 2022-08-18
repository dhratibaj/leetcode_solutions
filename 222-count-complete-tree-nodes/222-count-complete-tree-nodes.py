# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLHgt(self,root):
        hght = 0
        while(root):
            hght += 1
            root = root.left
        return hght
    
    def findRHgt(self,root):
        hght = 0
        while(root):
            hght += 1
            root = root.right
        return hght
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        lh = self.findLHgt(root.left)
        rh = self.findRHgt(root.right)
        if lh==rh: return(1<<(lh+1))-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
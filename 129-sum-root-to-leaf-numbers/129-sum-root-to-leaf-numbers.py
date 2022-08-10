# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def rootToleaf(self,root,s):
        if(not root.left and not root.right):
            s += str(root.val)
            self.ans += int(s)
            return
        curr = str(root.val)
        if(root.left!=None): self.rootToleaf(root.left,s+curr)
        if(root.right!=None): self.rootToleaf(root.right,s+curr)
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.rootToleaf(root,"")
        return self.ans
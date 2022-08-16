# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNodes(self,root,x,y,level,parents,currLevel,currParent):
        if(not root): return
        if(root.val==x):
            level[0] = currLevel
            parents[0] = currParent.val
        if(root.val==y):
            level[1] = currLevel
            parents[1] = currParent.val
        self.findNodes(root.left,x,y,level,parents,currLevel+1,root)
        self.findNodes(root.right,x,y,level,parents,currLevel+1,root)
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        level,parents = [-1,-1],[-1,-1]
        self.findNodes(root,x,y,level,parents,0,TreeNode(-1))
        if(level[0]==level[1] and parents[0]!=parents[1]): return True
        return False
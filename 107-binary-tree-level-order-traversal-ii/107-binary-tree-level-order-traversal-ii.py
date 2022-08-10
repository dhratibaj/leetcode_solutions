# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Levelorder(self,root,level,ans):
        if(not root): return
        if(level==len(ans)): ans.append([])
        ans[level].append(root.val)
        self.Levelorder(root.left,level+1,ans)
        self.Levelorder(root.right,level+1,ans)
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.Levelorder(root,0,ans)
        return ans[::-1]
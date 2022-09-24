# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root == None: return None
            targetSum -= root.val
            path.append(root.val)
            if root.left == None and root.right == None:  # Is leaf node
                if targetSum == 0:  # Found a valid path
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack
    
        ans = []
        dfs(root, targetSum, [])
        return ans
    
#     def helper(self,root,t,res,temp):
#         if(not root): return
#         t -= root.val
#         temp.append(root.val)
#         if not root.left and not root.right:
#             if t==0:
#                 res.append(list(temp))
#                 return
#         else:
#             self.helper(root.left,t,res,temp)
#             self.helper(root.right,t,res,temp)
#         temp.pop()
        
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         res = []
#         # targetSum -= root.val
#         # self.helper(root.left,targetSum,res,[root.val])
#         # self.helper(root.right,targetSum,res,[root.val])
#         self.helper(root,targetSum,res,[])
#         return res
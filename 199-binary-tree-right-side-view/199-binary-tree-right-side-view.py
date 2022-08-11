# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view
        
#--------------------all test cases passed recursive(combine right & left)---------------------------------------        
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         right = self.rightSideView(root.right)
#         left = self.rightSideView(root.left)
#         return [root.val] + right + left[len(right):]
        
#------------------------------37 / 216 test cases passed----------------------------------------------------        
# class Solution:
#     def view(self,root,ans,s,level):
#         if(not root): return
#         if(level not in s):
#             s.add(level)
#             ans.append(root.val)
#         self.view(root.right,ans,s,level+1)
#         self.view(root.right,ans,s,level+1)
#         return
    
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         s = set()
#         self.view(root,ans,s,0)
#         return ans
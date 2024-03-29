# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        deque, res = deque(), []
        if root:
            deque.append(root)
        while deque:
            level, size = [], len(deque)
            for _ in range(size):
                node = deque.popleft()
                level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(level)
        return res
    
    
#-------------------------------python recursive approach------------------------------------------
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def dfs(self, root, level, res):
#         if not root: return 
#         if len(res) < level+1: res.append([])
#         res[level].append(root.val)
#         self.dfs(root.left, level+1, res)
#         self.dfs(root.right, level+1, res)
    
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
#         self.dfs(root, 0, res)
#         return res
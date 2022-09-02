# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        deque, res = deque(), []
        if root:
            deque.append(root)
        while deque:
            level, size, c = 0.0, len(deque), 0.0
            for _ in range(size):
                node = deque.popleft()
                level += node.val
                c += 1.0
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(level/c)
        return res
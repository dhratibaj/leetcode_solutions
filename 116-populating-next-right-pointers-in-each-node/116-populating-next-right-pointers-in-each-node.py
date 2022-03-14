"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        
        while q:
            r = len(q)-1
            for i in range(len(q)):
                current = q.popleft()
                if r > 0:
                    current.next = q[0]
                    r -= 1
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return root 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self, main):
        if main==None:
            return [None, None]

        lef = self.convert(main.left)
        rig = self.convert(main.right)

        if lef[1]!=None:
            lef[1].right = main

        main.right = rig[0]
        main.left = None

        if lef[0]==None:
            lef[0] = main
        if rig[1]==None:
            rig[1] = main

        return [lef[0], rig[1]] # toppest node, rightmost node after conversion
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.convert(root)[0]
        
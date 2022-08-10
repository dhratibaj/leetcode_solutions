# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = float('-inf')
    def maxPath(self,root):
        if(not root): return 0
        l = max(0,self.maxPath(root.left))
        r = max(0,self.maxPath(root.right))
        self.maxi = max(self.maxi,l+r+root.val)
        return root.val+max(l,r)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath(root)
        return self.maxi


#--------------------------------cpp--------------------------------------------
# class Solution {
# public:
#     int maxPath(TreeNode* root, int& maxi){
#         if(!root) return 0;
#         int left = max(0,maxPath(root->left,maxi));
#         int right = max(0,maxPath(root->right,maxi));
#         maxi = max(maxi,left+right+root->val);
#         return root->val + max(left,right);
#     }
    
#     int maxPathSum(TreeNode* root) {
#         int maxi = INT_MIN;
#         maxPath(root,maxi);
#         return maxi;
#     }
# };
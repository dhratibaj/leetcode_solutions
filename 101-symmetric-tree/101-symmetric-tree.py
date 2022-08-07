# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self,l,r):
        if l==None and r==None: return True
        elif l==None or r==None: return False
        elif l.val!=r.val: return False
        return self.isMirror(l.left,r.right) and self.isMirror(l.right,r.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None: return True
        return self.isMirror(root.left,root.right)
        
        
#-------------------------------------------------cpp-------------------------------------------------------        
# /**
#  * Definition for a binary tree node.
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
#  * };
#  */
# class Solution {
# public:
#     bool isMirror(TreeNode* l,TreeNode* r){
#         if(l==NULL && r==NULL) return true;
#         else if(l==NULL||r==NULL) return false;
#         else if(l->val!=r->val) return false;
#         return isMirror(l->left,r->right) && isMirror(l->right,r->left);
#     }
    
#     bool isSymmetric(TreeNode* root) {
#         if(root==NULL) return true;
#         return isMirror(root->left,root->right);
#     }
# };
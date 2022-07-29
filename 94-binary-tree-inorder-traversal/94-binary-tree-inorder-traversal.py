# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Inorder(self,root,ans):
        if root == None:
            return 
        self.Inorder(root.left,ans)
        ans.append(root.val)
        self.Inorder(root.right,ans)
        return
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.Inorder(root,ans)
        return ans
        
    
#----------------------------------Cpp-----------------------------------------------
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
#     void Inorder(TreeNode* root, vector<int> &ans)
#     {
#         if(root == NULL) 
#             return;
#         Inorder(root->left,ans);
#         ans.push_back(root->val);
#         Inorder(root->right,ans);
#         return;
#     }
    
#     vector<int> inorderTraversal(TreeNode* root) {
#         vector<int> ans;
#         Inorder(root,ans);
#         return ans;
#     }
# };
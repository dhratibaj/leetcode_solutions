/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

//-------------------MORRIS INORDER Traversal--------------------------------------------------
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inorder; TreeNode *cur = root;
        while(cur){
            if(cur->left==NULL){
                inorder.push_back(cur->val);
                cur = cur->right;
            }
            else{
                TreeNode *prev = cur->left;
                while(prev->right && prev->right!=cur)
                    prev = prev->right;
                if(prev->right==NULL){
                    prev->right = cur;
                    cur = cur->left;
                }
                else{
                    prev->right = NULL;
                    inorder.push_back(cur->val);
                    cur=cur->right;
                }
            }
        }
        return inorder;
    }
};
// -------------------------Normal Recursion------------------------------
// class Solution {
// public:
//     void Inorder(TreeNode* root, vector<int> &ans)
//     {
//         if(root == NULL) 
//             return;
//         Inorder(root->left,ans);
//         ans.push_back(root->val);
//         Inorder(root->right,ans);
//         return;
//     }
    
//     vector<int> inorderTraversal(TreeNode* root) {
//         vector<int> ans;
//         Inorder(root,ans);
//         return ans;
//     }
// };
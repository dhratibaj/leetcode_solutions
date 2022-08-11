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
class Solution {
public:
    int leftLeaf(TreeNode* root, bool leaf){
        if(!root) return 0;
        if(!root->left && !root->right && leaf) return root->val;
        int ls = leftLeaf(root->left,true);
        int rs = leftLeaf(root->right,false);
        return ls+rs;
    }
    
    int sumOfLeftLeaves(TreeNode* root) {
        return leftLeaf(root,false);
    }
};
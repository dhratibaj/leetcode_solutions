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
    void rootToleaf(TreeNode* root, string currStr, int& ans){
        if(!root->left && !root->right){
            currStr += to_string(root->val);
            ans += stoi(currStr,0);
            return;
        }
        string curr = to_string(root->val);
        if(root->left!=NULL) rootToleaf(root->left,currStr+curr,ans);
        if(root->right!=NULL) rootToleaf(root->right,currStr+curr,ans);
    }
    
    int sumNumbers(TreeNode* root) {
        int ans = 0;
        rootToleaf(root,"",ans);
        return ans;
    }
};
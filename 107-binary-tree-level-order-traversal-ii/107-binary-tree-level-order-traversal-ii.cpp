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
    vector<vector<int>> ans;
public:
    void Levelorder(TreeNode* root, int level){
        if(!root) return;
        if(level==ans.size()) ans.push_back(vector<int>());
        ans[level].push_back(root->val);
        Levelorder(root->left,level+1);
        Levelorder(root->right,level+1);
    }
    
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        Levelorder(root,0);
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
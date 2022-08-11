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
    void view(TreeNode* root,vector<int>& res, set<int>& s, int level){
        if(!root) return;
        if(s.find(level)==s.end()){
            s.insert(level);
            res.push_back(root->val);
        }
        view(root->right,res,s,level+1);
        view(root->left,res,s,level+1);
        return;
    }
    
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        set<int> s;
        view(root,res,s,0);
        return res;
    }
};
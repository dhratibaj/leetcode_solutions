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
    void rootToLeaf(TreeNode* root, string s, int* ans){
        if(!root->left && !root->right){
            s += to_string(root->val);
            ans[0]+=stoi(s,0,2);
            return;
        }
        string curr = to_string(root->val);
        if(root->left) rootToLeaf(root->left,s+curr,ans);
        if(root->right) rootToLeaf(root->right,s+curr,ans);
    }
    
    int sumRootToLeaf(TreeNode* root) {
        int* ans = new int[1];
        ans[0] = 0;
        rootToLeaf(root,"",ans);
        return ans[0];
    }
};

//--------------Another approach-------------------------------------------------------------
// class Solution {
//     int sumRootToLeaf(TreeNode* root, int sum){
//         if(!root) return 0;
//         sum = (2 * sum) + root->val;
//         if(!root->left && !root->right) return sum;
//         return sumRootToLeaf(root->left, sum) + sumRootToLeaf(root->right, sum);
//     }
// public:
//     int sumRootToLeaf(TreeNode* root) {
//         return sumRootToLeaf(root, 0);
//     }
    
// };
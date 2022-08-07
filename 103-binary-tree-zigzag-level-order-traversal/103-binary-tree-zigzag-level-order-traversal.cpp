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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(!root) return result;
        queue<TreeNode*> Qnodes;
        Qnodes.push(root);
        bool left_right = true;
        while(!Qnodes.empty()){
            int size = Qnodes.size();
            vector<int> row(size);
            for(int i=0;i<size;i++){
                TreeNode* node = Qnodes.front();
                Qnodes.pop();
                    //find pos to fill node's value
                int index =(left_right)?i:(size-1-i);
                row[index] = node->val;
                if(node->left) Qnodes.push(node->left);
                if(node->right) Qnodes.push(node->right);
            }
            //after this level
            left_right = !left_right;
            result.push_back(row);
        }
        return result;
    }
};
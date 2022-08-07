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
        vector<vector<int>> list, res;
        traversal(list, root, 1);
        for (int i = 0; i < list.size(); i++) {
            res.push_back(vector<int>());
            vector<int> tmp = list[i];
            if (i % 2 == 0) {
                for (int j = 0; j < tmp.size(); j++) {
                    res[i].push_back(tmp[j]);
                }
            } else {
                for (int j = tmp.size() - 1; j >= 0; j--) {
                    res[i].push_back(tmp[j]);
                }
            }
        }
        return res;
    }
    void traversal(vector<vector<int>>& list, TreeNode* root, int level) {
        if (!root) {
            return;
        }
        if (list.size() < level) {
            list.push_back(vector<int>());
        }
        list[level - 1].push_back(root->val);
        traversal(list, root->left, level + 1);
        traversal(list, root->right, level + 1);
    }
};



//------------------------------------cpp iterative approach---------------------------------------
// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//  *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//  *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
//  * };
//  */
// class Solution {
// public:
//     vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
//         vector<vector<int>> result;
//         if(!root) return result;
//         queue<TreeNode*> Qnodes;
//         Qnodes.push(root);
//         bool left_right = true;
//         while(!Qnodes.empty()){
//             int size = Qnodes.size();
//             vector<int> row(size);
//             for(int i=0;i<size;i++){
//                 TreeNode* node = Qnodes.front();
//                 Qnodes.pop();
//                     //find pos to fill node's value
//                 int index =(left_right)?i:(size-1-i);
//                 row[index] = node->val;
//                 if(node->left) Qnodes.push(node->left);
//                 if(node->right) Qnodes.push(node->right);
//             }
//             //after this level
//             left_right = !left_right;
//             result.push_back(row);
//         }
//         return result;
//     }
// };
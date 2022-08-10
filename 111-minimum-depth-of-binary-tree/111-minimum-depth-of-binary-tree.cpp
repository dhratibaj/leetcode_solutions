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
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        if(root->left==NULL || root->right==NULL)
            return max(minDepth(root->left),minDepth(root->right))+1;
        else
            return min(minDepth(root->left),minDepth(root->right))+1;
    }
};


// # Definition for a binary tree node.
// # class TreeNode:
// #     def __init__(self, val=0, left=None, right=None):
// #         self.val = val
// #         self.left = left
// #         self.right = right
// class Solution:
//     def minDepth(self, root: Optional[TreeNode]) -> int:
//         if(not root): return 0
//         if None in [root.left, root.right]:
//             return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
//         else:
//             return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
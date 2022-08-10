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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(!root) return false;
        targetSum -= root->val;
        if(!root->left && !root->right)
            if(targetSum==0) return true;
        return hasPathSum(root->left,targetSum) || hasPathSum(root->right,targetSum);
    }
};

// # Definition for a binary tree node.
// # class TreeNode:
// #     def __init__(self, val=0, left=None, right=None):
// #         self.val = val
// #         self.left = left
// #         self.right = right
// class Solution:
//     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
//         if not root:
//             return False
//         targetSum-=root.val
//         if not root.left and not root.right:
//             if targetSum == 0:
//                 return True
//         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
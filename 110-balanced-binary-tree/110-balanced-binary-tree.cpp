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
    int check(TreeNode* root){
        if(!root) return 0;
        int lh = check(root->left);
        int rh = check(root->right);
        if(lh==-1 || rh==-1 || abs(lh-rh)>1) return -1;
        return max(lh,rh)+1;
    }
    
    bool isBalanced(TreeNode* root) {
        return check(root)!=-1;
    }
};


// # Definition for a binary tree node.
// # class TreeNode:
// #     def __init__(self, val=0, left=None, right=None):
// #         self.val = val
// #         self.left = left
// #         self.right = right
// class Solution:
//     def check(self,root):
//         if(not root): return 0
//         lh = self.check(root.left)
//         rh = self.check(root.right)
//         if(lh==-1 or rh==-1 or abs(lh-rh)>1): return -1
//         return max(lh,rh)+1
    
//     def isBalanced(self, root: Optional[TreeNode]) -> bool:
//         return self.check(root)!=-1
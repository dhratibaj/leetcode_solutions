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
    void findNodes(TreeNode* root, int x, int y, int level[2], int parent[2], int currLevel, TreeNode* currParent){
        if(!root) return;
        if(root->val==x){
            level[0]=currLevel;
            parent[0]=currParent->val;
        }
        if(root->val==y){
            level[1]=currLevel;
            parent[1]=currParent->val;
        }
        findNodes(root->left,x,y,level,parent,currLevel+1,root);
        findNodes(root->right,x,y,level,parent,currLevel+1,root);
    }
    
    bool isCousins(TreeNode* root, int x, int y) {
        int level[2]={-1,-1}, parent[2]={-1,-1};
        findNodes(root,x,y,level,parent,0,new TreeNode(-1));
        if(level[0]==level[1] && parent[0]!=parent[1]) return true;
        return false;
    }
};

// def dept(self, node, d, par, x, y):
//         if not node: return 
//         if node.val == x:
//             self.a = d
//             self.aparent= par
//         elif node.val == y:
//             self.b = d
//             self.bparent= par
//         self.dept(node.left, d+1, node, x, y)
//         self.dept(node.right, d+1, node, x, y)
        
//     def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
//         self.dept(root, 0, None, x, y)
//         return self.a == self.b and self.aparent != self.bparent
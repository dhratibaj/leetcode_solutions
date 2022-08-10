/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    void pre(Node* root,vector<int>& ans){
        if(!root) return;
        ans.push_back(root->val);
        for(auto child: root->children)
            pre(child,ans);
        return;
    }
    
    vector<int> preorder(Node* root) {
        vector<int> ans;
        pre(root,ans);
        return ans;
    }
};

// """
// # Definition for a Node.
// class Node:
//     def __init__(self, val=None, children=None):
//         self.val = val
//         self.children = children
// """

// class Solution:
//     def Pre(self,root,ans):
//         if(not root): return 
//         ans.append(root.val)
//         for i in range(len(root.children)):
//             self.Pre(root.children[i],ans)
//         return
    
//     def preorder(self, root: 'Node') -> List[int]:
//         ans = []
//         self.Pre(root,ans)
//         return ans
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
    void post(Node* root,vector<int>& ans){
        if(!root) return ;
        for(auto child: root->children)
            post(child,ans);
        ans.push_back(root->val);
        return;
    }
    
    vector<int> postorder(Node* root) {
        vector<int> ans;
        post(root,ans);
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
//     def post(self,root,ans):
//         if(not root): return 
//         for i in range(len(root.children)):
//             self.post(root.children[i],ans)
//         ans.append(root.val)
//         return
    
//     def postorder(self, root: 'Node') -> List[int]:
//         ans = []
//         self.post(root,ans)
//         return ans
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
    int maxDepth(Node* root) {
        if(!root) return 0;
        int ans = 0;
        for(auto child: root->children)
            ans = max(ans,maxDepth(child));
        return 1+ans;
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
//     def maxDepth(self, root: 'Node') -> int:
//         if(not root): return 0
//         ans = 0
//         for i in range(len(root.children)):
//             temp = self.maxDepth(root.children[i])
//             ans = max(ans,temp)
//         return ans + 1
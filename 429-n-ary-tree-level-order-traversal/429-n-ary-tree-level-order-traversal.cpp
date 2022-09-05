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
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res;
        queue<Node*> q;
        if(!root) return res;
        q.push(root);
        while(!q.empty()){
            int n =q.size();
            vector<int> level;
            while(n>0){
                Node* curr = q.front();
                q.pop();
                level.push_back(curr->val);
                n--;
                for(auto child: curr->children)
                    q.push(child);
            }
            res.push_back(level);
        }
        return res;
    }
};
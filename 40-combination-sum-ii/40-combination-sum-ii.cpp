class Solution {
public:
    void findAll(vector<int>& a, int t, int idx, vector<vector<int>> &res,vector<int> &ans){
        if(t==0){
            res.push_back(ans);
            return;
        }
        for(int i=idx;i<a.size();i++){
            if(i>idx && a[i]==a[i-1]) continue;
            if(a[i]>t) break;
            ans.push_back(a[i]);
            findAll(a,t-a[i],i+1,res,ans);
            ans.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> ans;
        sort(candidates.begin(),candidates.end());
        findAll(candidates,target,0,res,ans);
        return res;
    }
};
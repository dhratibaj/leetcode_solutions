class Solution {
public:
    void solve(vector<int>& arr, int t, int idx, vector<vector<int>>&res, vector<int>&ans){
        if(t==0){ res.push_back(ans); return;}
        for(int i=idx;i<arr.size();i++){
            if(i>idx && arr[i]==arr[i-1]) continue;
            if(arr[i]>t)break;
            ans.push_back(arr[i]);
            solve(arr,t-arr[i],i+1,res,ans);
            ans.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> ans;
        sort(candidates.begin(),candidates.end());
        solve(candidates,target,0,res,ans);
        return res;
    }
};
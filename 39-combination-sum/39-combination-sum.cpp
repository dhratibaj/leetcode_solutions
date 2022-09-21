class Solution {
public:
    void solve(int idx, vector<int> arr, int t, vector<vector<int>> &res, vector<int> &ans){
        if(idx==arr.size())
        {   if(t==0)
                res.push_back(ans);
            return;
         }
        if(arr[idx]<=t){
            ans.push_back(arr[idx]);
            solve(idx,arr,t-arr[idx],res,ans);
            ans.pop_back();
        }
        solve(idx+1,arr,t,res,ans);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> ans;
        solve(0,candidates,target,res,ans);
        return res;
    }
};
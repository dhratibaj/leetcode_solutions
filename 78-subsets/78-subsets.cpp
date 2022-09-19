class Solution {
public:
    void solve(vector<int> nums, int n, vector<vector<int>> &ans,int idx, vector<int> &res){
        if(idx==n) {ans.push_back(res); return;} 
        else{
            res.push_back(nums[idx]);
            solve(nums, n, ans, idx+1, res);
            res.pop_back();
            solve(nums, n, ans, idx+1, res);
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> res;
        solve(nums,nums.size(),ans,0,res);
        return ans;
    }
};
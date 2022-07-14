class Solution {
public:
    void func(int i,vector<int>& a,int t,vector<vector<int>>& res,vector<int>& arr){
        if(i==a.size()){
            if(t==0)
                res.push_back(arr);
            return;
        }
        if(a[i]<=t){
            arr.push_back(a[i]);
            func(i,a,t-a[i],res,arr);
            arr.pop_back();
        }
        func(i+1,a,t,res,arr);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> arr;
        func(0,candidates,target,res,arr);
        return res;
    }
};
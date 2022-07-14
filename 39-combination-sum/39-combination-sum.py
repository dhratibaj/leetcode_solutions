# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []
#         self.backtracking(res,0,[],nums,target)
#         return res
#     def backtracking(self,res,start,subset,nums,target):
#         if (start == len(nums)):
#             if target == 0:
#                 res.append(list(subset))
#             return
#         if nums[start] <= target:
#             subset.append(nums[start])
#             self.backtracking(res,start,subset,nums,target-nums[start])
#             subset.pop() 
#         self.backtracking(res,start+1,subset,nums,target)
#-------------------------------------------------------------------------------------------

class Solution:
    def func(self,i,a,t,res,arr):
        if i==len(a):
            if t==0:
                res.append(list(arr))
            return
        if a[i]<=t:
            arr.append(a[i])
            self.func(i,a,t-a[i],res,arr)
            arr.pop()
        self.func(i+1,a,t,res,arr)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.func(0,candidates,target,res,[])
        return res
#-----------------------------------------C++--------------------------------------------------

# class Solution {
# public:
#     void func(int i,vector<int>& a,int t,vector<vector<int>>& res,vector<int>& arr){
#         if(i==a.size()){
#             if(t==0)
#                 res.push_back(arr);
#             return;
#         }
#         if(a[i]<=t){
#             arr.push_back(a[i]);
#             func(i,a,t-a[i],res,arr);
#             arr.pop_back();
#         }
#         func(i+1,a,t,res,arr);
#     }
    
#     vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
#         vector<vector<int>> res;
#         vector<int> arr;
#         func(0,candidates,target,res,arr);
#         return res;
#     }
# };
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0,n=nums.size();
        for(int fast=0;fast<n;fast++){
            if(nums[fast]!=0 && nums[slow]==0)
                swap(nums[slow],nums[fast]);
            if(nums[slow]!=0)
                slow += 1;
        }
    }
};
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n=nums.size(),c=0;
        for(int i=0;i<n;i++){
            if(nums[i]==0){
                c += 1;
                continue;
            }
            nums[i-c] = nums[i];
        }
        for(int i=n-c;i<n;i++)
            nums[i]=0;
    }
};
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> mpp;
        for(auto i: nums){
            if(mpp.find(i)!=mpp.end())
                return true;
            else
                mpp[i] = 1;
        }
        return false;
    }
};
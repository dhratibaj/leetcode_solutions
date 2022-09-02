class Solution {
public:
    int arraySign(vector<int>& nums) {
        int flag = 0;
        for(auto i:nums)
        {if(i==0) return 0;
        else if(i<0) flag++;}
        if(flag%2==0) return 1;
        else return -1;
    }
};
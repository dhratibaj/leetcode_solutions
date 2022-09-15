class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int d = arr[1]-arr[0];
        bool val = true;
        for(int i=2;i<arr.size();i++)
            if(d!=arr[i]-arr[i-1])
            {val = false;break;}
        return val;
    }
};
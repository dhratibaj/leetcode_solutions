class Solution {
public:
    int sum(vector<int> list){
        int s = 0;
        for(auto i: list)
            s += i;
        return s;
    }
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxx = 0;
        for(auto list: accounts)
            maxx = max(maxx,sum(list));
        return maxx;
    }
};
class Solution {
public:
    int countOdds(int low, int high) {
        if (low%2==0)
            if (high%2==0)
                return int((high-low)/2);
        return int((high-low)/2)+1;
    }
};
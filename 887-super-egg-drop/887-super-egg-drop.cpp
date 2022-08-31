class Solution {
public:
    int superEggDrop(int k, int n) {
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
        int m = 0;
        while (dp[m][k] < n) {
            m++;
            for (int x = 1; x <= k; ++x)
                dp[m][x] = dp[m - 1][x - 1] + dp[m - 1][x] + 1;
        }
        return m;
    }
};
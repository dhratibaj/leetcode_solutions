class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int sum = 0,i,j,n=mat.size();
        for(i=0;i<n;i++)
            sum += mat[i][i];
        i=0;j=n-1;
        while(i<n){
            sum += mat[i][j];
            i++; j--;
        }
        if(n%2!=0) sum -= mat[n/2][n/2];
        return sum;
    }
};
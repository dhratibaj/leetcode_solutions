class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for i in range(x)]for x in range(1,query_row+2)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(len(dp[i])):
                temp = (dp[i][j]-1)/2
                if temp>0:
                    dp[i+1][j]+=temp
                    dp[i+1][j+1]+=temp
        return dp[query_row][query_glass] if dp[query_row][query_glass]<=1 else 1
        
        #-----------------------Shows TLE with this one
        # if poured == 0:
        #     return 0
        # l = []
        # l.append(poured)
        # while(query_row>0):
        #     temp = []
        #     temp.append(max((l[0]-1)/2,0))
        #     for i in range(1,len(l)):
        #         temp.append(max((l[i-1]-1)/2,0)+max((l[i]-1)/2,0))
        #     temp.append(temp[0])
        #     l = temp
        # return min(1,l[query_glass])
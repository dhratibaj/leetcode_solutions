class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x1,x2,y1,y2;
        bool val = true;
        x1 = coordinates[0][0], y1 = coordinates[0][1];
        x2 = coordinates[1][0], y2 = coordinates[1][1];
        for(int i=2;i<coordinates.size();i++){
            int x=coordinates[i][0], y=coordinates[i][1];
            if((y2-y1)*(x1-x)!=(y1-y)*(x2-x1))
                val = false;
        }
        return val;
    }
};
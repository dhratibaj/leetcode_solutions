class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        queue<int> q;
        q.push(start);
        while(size(q)) {
            int cur = q.front(); q.pop();
            if(arr[cur] == 0) return true;                        
            if(arr[cur] < 0)  continue;                          
            if(cur + arr[cur] < size(arr)) q.push(cur+arr[cur]);    
            if(cur - arr[cur] >= 0)      q.push(cur-arr[cur]);    
            arr[cur] *= -1;                                       
        }
        return false;        
    }
};
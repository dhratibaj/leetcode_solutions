class Solution {
public:
    int next(int n){
        int sum=0;
        while(n){
            int i = n%10;
            sum += i*i;
            n/=10;
        }
        return sum;
    }
    bool isHappy(int n) {
       set<int> seen;
        while(true){
            if(seen.find(n)!=seen.end()) return false;
            else if(n==1) return true;
            else
            {
                seen.insert(n);
                n = next(n);
            }
        }
    }
};
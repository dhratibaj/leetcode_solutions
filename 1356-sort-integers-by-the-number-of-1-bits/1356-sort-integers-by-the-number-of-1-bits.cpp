class Solution {
public:
    static bool compare(int a, int b){
        bitset<32> b1(a);
        bitset<32> b2(b);
        if(b1.count() != b2.count()){
            return b1.count() < b2.count();
        }
        else  return a < b;
    }
    vector<int> sortByBits(vector<int>& arr) {
        std::sort(arr.begin(), arr.end(), compare);
        return arr;
    }
};
// class Solution {
// public:
//     static bool compare(const int& a, const int& b){
//         int c1 = __builtin_popcount(a);
//         int c2 = __builtin_popcount(b);
//         if(c1 == c2)
//             return a < b;
//         return c1 < c2;
//     }
//     vector<int> sortByBits(vector<int>& arr) {
//         std::sort(arr.begin(),arr.end(), compare);
//         return arr;
//     }
// };


// class Solution {
// public:
//     int countsetbits(int n)
//     {
//         int c=0;
//         while(n)
//         {
//             if(n%2!=0)
//             c++;
//             n/=2;
//         }
//         return c;
//     }
//     vector<int> sortByBits(vector<int>& arr) {
//         map<int, vector<int>>mp;
//         vector<int>v;
//         sort(arr.begin(), arr.end());
//         for(int i=0; i<arr.size(); i++)
//         mp[countsetbits(arr[i])].push_back(arr[i]);
//         for(auto it=mp.begin(); it!=mp.end(); it++)
//         {
//             for(int a:it->second)
//             v.push_back(a);
//         }
//         return v;
//     }
// };
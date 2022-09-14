class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> mp1, mp2;
        for(auto i:s){
            if(mp1.find(i)!=mp1.end())
                mp1[i] += 1;
            else
            mp1[i] = 1;
        }
        for(auto i:t){
            if(mp2.find(i)!=mp2.end())
                mp2[i] += 1;
            else
            mp2[i] = 1;
        }
        bool val = true;
        if(mp2.size()>=mp1.size())
        for(auto i: mp2){
            if(mp1.find(i.first)==mp1.end() || mp1[i.first]!=mp2[i.first])
                val = false;
        }
        else
            for(auto i: mp1){
            if(mp2.find(i.first)==mp2.end() || mp1[i.first]!=mp2[i.first])
                val = false;
        }
        return val;
    }
};
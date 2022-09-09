class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char,int> m1,m2;
        char res;
        for(auto i: t){
            if(m1.find(i)!=m1.end()) m1[i]+=1;
            else m1[i] = 1;
        }
        for(auto i: s){
            if(m2.find(i)!=m2.end()) m2[i]+=1;
            else m2[i] = 1;
        }
        for(auto i: m1)
            if(m2.find(i.first)==m2.end() || m1[i.first]!=m2[i.first])
                res = i.first;
        return res;
    }
};
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int count=0;
        vector<int> idx;
        for(int i=0;i<s1.size();i++){
            if(s1[i]!=s2[i]){
                count ++;
                idx.push_back(i);
            }
            if(count>2) return false;
        }
        if(!idx.size()) return true;
        else if(count==2) if(s1[idx[0]]==s2[idx[1]] && s1[idx[1]]==s2[idx[0]]) return true;
        return false;
    }
};
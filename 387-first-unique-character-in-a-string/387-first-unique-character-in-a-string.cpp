class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char,int> map;
        for(int i=0; i<s.length(); i++){
            if(map.count(s[i])==0)
                map[s[i]] = 1;
            else
                map[s[i]]++;   
        }
        for(int i=0; i<s.length(); i++)
            if(map[s.at(i)] == 1)
                return i;
        return -1;
        //-------------Another approach---------------------------------------
		// vector<int> v(26,0);
		// for(char c : s) v[c - 'a']++;
		// for(int i = 0; i < s.length(); i++){
		// 	if(v[s[i] - 'a'] == 1) return i;
		// }
		// return -1;
    }
};
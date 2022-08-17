class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        string l[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        set<string> res;
        for(int i=0;i<words.size();i++){
            string s = "";
            for(int j=0;j<words[i].length();j++)
                s+=l[words[i][j]-'a'];
            res.insert(s);
            }
        return res.size();
    }
};
class Solution {
public:
    string toLowerCase(string s) {
        for(int i=0;i<s.length();i++)
            if(s[i]>='A'&&s[i]<='Z')
            s[i] = s[i] + 32;
        return s;
    }
};

// class Solution {
// public:
//     string toLowerCase(string s) {
//         for(int i=0;i<s.length();i++)
//             s[i] = tolower(s[i]);
//         return s;
//     }
// };

// class Solution {
// public:
//     string toLowerCase(string s) {
//         transform(s.begin(),s.end(),s.begin(),::tolower);
//         return s;
//     }
// };
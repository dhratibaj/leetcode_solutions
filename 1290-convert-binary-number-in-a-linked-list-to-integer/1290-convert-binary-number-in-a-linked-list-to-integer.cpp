/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int BinToDec(string s){
        int n = s.length(),i=0;
        int j = n-1,sum=0;
        while(i<n){
            if(s[i]=='1')
                sum += pow(2,j);
            i++;j--;
        }
       return sum; 
    }
    
    int getDecimalValue(ListNode* head) {
        string s = "";
        while(head){
            s += to_string(head->val);
            head = head->next;
        }
        return BinToDec(s);
    }
};
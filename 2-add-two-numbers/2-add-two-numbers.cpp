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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyNode;  ListNode* head;
        dummyNode = head = new ListNode(-1);
        if(!l1) return l2;
        if(!l2) return l1;
        int carry = 0;
        while(l1||l2){
            int first = l1?l1->val:0;
            int second = l2?l2->val:0;
            int total = first+second+carry;
            carry = total/10;
            total %= 10;
            ListNode* newNode= new ListNode(total);
            dummyNode->next = newNode;
            dummyNode = dummyNode->next;
            l1 = l1?l1->next:l1;
            l2 = l2?l2->next:l2;
        }
        if(carry)
            dummyNode->next = new ListNode(1);
        return head->next;
    }
};
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i == ")":
                ans += stack.pop()+ max(ans,1)   
            else:
                stack.append(ans)
                ans = 0   
        return ans
class Solution:
    def isValid(self, s: str) -> bool:
        dic,stack = {')': '(', ']': '[', '}': '{'}, []
        for i in s:
            if stack and dic.get(i) == stack[-1]: stack.pop()
            else:                                 
                if i in dic: return False         
                stack.append(i)       
        return not stack
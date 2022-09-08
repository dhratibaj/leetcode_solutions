class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        n,i = len(command),0
        while(i<n):
            if command[i]=='G':
                res += 'G'
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                res += 'o'
                i+= 2
            else:
                res += 'al'
                i += 4
        return res
        
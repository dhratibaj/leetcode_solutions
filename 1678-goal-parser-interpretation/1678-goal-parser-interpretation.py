class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        for i in range(len(command)):
            if command[i]=='G':
                res += 'G'
            elif command[i:i+2] == '()':
                res += 'o'
            elif i+3 < len(command):
                if command[i:i+4] == '(al)':
                    res += 'al'
        return res
class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(10,27):
            s = s.replace(str(i)+"#", chr(ord("j")+(i-10)))
        for i in range(1,10):
            s = s.replace(str(i),chr(ord("a")+(i-1) ));
        return(s)
        
        # res = ''
        # if s[-1] == '#':
        #     for i in range(len(s)-2):
        #         if s[i+2] == "#":
        #             res += str(97+int(s[i:i+2])-1)
        #         else:
        #             res += str(97+int(s[i])-1)
        # else:
        #     for i in range(len(s)):
        #         if i!=len(s)-3:
        #             if s[i+2] == "#":
        #                 res += str(97+int(s[i:i+2])-1)
        #             else:
        #                 res += str(97+int(s[i])-1)
        # return res
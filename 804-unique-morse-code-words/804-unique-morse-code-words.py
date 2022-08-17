class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for i in words:
            s = ""
            for j in i:
                s+=l[ord(j)-ord('a')]
            res.add(s)
        return len(res)
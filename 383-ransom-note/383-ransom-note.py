class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = 0
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,"",1)
                c += 1
        return c == len(ransomNote)
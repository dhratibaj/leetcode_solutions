class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            if order[i] not in d:
                d[order[i]] = i
        l = [[d[i] for i in word] for word in words]
        return l == sorted(l)
        
            
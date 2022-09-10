class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda word:[order.index(c) for c in word])
        
        # d = {}
        # for i in range(len(order)):
        #     if order[i] not in d:
        #         d[order[i]] = i
        # l = [[d[i] for i in word] for word in words]
        # return l == sorted(l)
        
            
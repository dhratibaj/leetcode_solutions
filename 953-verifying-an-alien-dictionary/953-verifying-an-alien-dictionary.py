class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {ch: i for i, ch in enumerate(order)}
        prev_repr = list(hm[ch] for ch in words[0])
        for i in range(1, len(words)):
            cur_repr = list(hm[ch] for ch in words[i])
            if cur_repr < prev_repr:
                return False
            prev_repr = cur_repr
        return True
        
        # return words == sorted(words, key=lambda word:[order.index(c) for c in word])
        
        # d = {}
        # for i in range(len(order)):
        #     if order[i] not in d:
        #         d[order[i]] = i
        # l = [[d[i] for i in word] for word in words]
        # return l == sorted(l)
        
            
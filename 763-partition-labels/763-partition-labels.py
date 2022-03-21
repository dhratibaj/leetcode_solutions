class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ind = end = 0
        r = []
        l = len(s)
        while end < l:
            ch = s[ind]
            end = s.rfind(ch) + 1
            ex = True
            while ex:
                ex = False
                d = dict.fromkeys(s[ind:end])
                for c in d:
                    endn = s.rfind(c) + 1
                    if endn > end:
                        end = endn
                        ex = True
                        break
            r.append(end-ind)
            ind = end
        return r
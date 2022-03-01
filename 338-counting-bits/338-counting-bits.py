def bitsoncount(x):
    return bin(x).count('1')
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(bitsoncount(i))
        return ans
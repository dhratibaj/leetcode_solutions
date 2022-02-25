class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2==0:
            if high%2==0:
                return int((high-low)/2)
        return ((high-low)//2)+1
                
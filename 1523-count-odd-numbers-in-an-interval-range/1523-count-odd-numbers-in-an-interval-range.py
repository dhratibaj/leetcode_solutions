class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((low&1))  +((high-low+1-(low&1))>>1)
                
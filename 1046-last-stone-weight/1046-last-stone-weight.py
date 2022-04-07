class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort()
            r = stones.pop()
            s = stones.pop()
            stones.append(r-s)
        return stones[0]
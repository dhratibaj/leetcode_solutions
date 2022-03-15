class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            j = 31 - i
            c = n & (1 << j)
            if c > 0:
                result += 1<< i 
        return result  
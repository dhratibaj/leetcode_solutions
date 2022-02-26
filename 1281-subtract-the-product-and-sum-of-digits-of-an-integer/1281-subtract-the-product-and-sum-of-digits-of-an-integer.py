class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sum = 1, 0
        while(n!=0):
            x = n%10
            prod *= x
            sum += x
            n = n//10
        return prod - sum
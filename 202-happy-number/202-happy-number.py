class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            tsum = 0
            while n>0:
                n,digit = divmod(n,10)
                tsum += digit**2
            return tsum
        slow = n
        fast = getNext(n)
        while fast!=1 and slow!=fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        return fast==1

    # ---------------------2nd approach--------------------------------------
        # def get_next(number):
        #     total_sum = 0
        #     while number > 0:
        #         number, digit = divmod(number, 10)
        #         total_sum += digit ** 2
        #     return total_sum  
        # while n != 1 and n != 4:
        #     n = get_next(n) 
        # return n == 1
    
    #-------------------------3rd brute force approach-------------------------------------------
        
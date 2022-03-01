class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0:
            if (high - low) % 2 == 0:
                return (high - low + 1) // 2 + 1
            else:
                return (high - low + 1) // 2
        elif low % 2 == 0:
                return (high - low + 1) // 2 
        
        #--------------2rd way---------44ms------------
        #return ((low&1))  +((high-low+1-(low&1))>>1) 
        
        #--------------3rd way---------50ms------------
        # if low%2==0:
        #     if high%2==0:
        #         return int((high-low)/2)
        #     return ((high-low)//2)+1
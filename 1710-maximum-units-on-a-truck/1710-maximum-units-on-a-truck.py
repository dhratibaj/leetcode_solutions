class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans,a = 0,0
        ar = []
        for x,y in boxTypes:
            ar.append(y)
            a += x
            ans += x*y
        if a < truckSize:
            return ans
        ans = 0
        ar.sort()
        while(truckSize):
            x = ar.pop()
            for i in boxTypes:
                if i[1] == x:
                    if i[0]>truckSize:
                        ans += truckSize*i[1]
                        truckSize = 0
                    else:
                        ans += i[0]*i[1]
                        truckSize -= i[0]
                    boxTypes.remove([i[0],i[1]])
        return ans
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True
        
        #-------------------------46 / 79 test cases passed -----------------------------
        # d = abs(coordinates[0][0] - coordinates[0][1])
        # for i in coordinates:
        #     if abs(i[0]-i[1]) != d: return False
        # return True
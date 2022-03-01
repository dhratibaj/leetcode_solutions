class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        if x2 != x1:
            
            slope = (y2-y1)/(x2-x1)
            c = y2 - (slope*x2)
            #y = slope*x + c
            for coordinate in coordinates:
                x, y = coordinate[0], coordinate[1]
                Y = slope*x + c
                if Y != y:
                    return False
            return True
        else:
            #equation: x = c i.e x1 or x2 in this case i.e the line is vertical/parallel to y axis => x should remain constant
            for coordinate in coordinates:
                x = coordinate[0]
                if x != x2:
                    return False
            return True
        
        # x1 = coordinates[0][0]-coordinates[1][0]
        # y1 = coordinates[0][1]-coordinates[1][1]
        # for i in range(2,len(coordinates)-1):
        #     if x1 != coordinates[i][0]-coordinates[i+1][0] or y1 != coordinates[i][1]-coordinates[i+1][1]:
        #         return False
        # return True
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        k = -1
        min_dist, curr_dist = sys.maxsize, -1
        for i in points:
            if i[0] == x or i[1] == y:
                curr_dist = abs(x-i[0])+abs(y-i[1])
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    k = points.index(i)
        return k
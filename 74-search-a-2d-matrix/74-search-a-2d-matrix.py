from collections import defaultdict
from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.find_row(matrix, target)
        if not row:
            return False
        else:
            return self.find_target(row, target)

	# find the row where target is located. If not possible, return False
    def find_row(self, matrix, target):
        lo = 0
        hi = len(matrix)

        while lo <= hi and (lo + hi) // 2 < len(matrix):
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return matrix[mid]
            elif matrix[mid][0] <= target:
                lo = mid + 1
            elif matrix[mid][-1] >= target:
                hi = mid - 1
        return False

    def find_target(self, row, target):
        lo = 0
        hi = len(row)

        while lo <= hi:
            mid = (lo + hi) // 2

            if row[mid] == target:
                return True
            elif target > row[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
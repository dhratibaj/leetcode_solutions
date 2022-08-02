import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:  
        m = sum(matrix, [])         # convert matrix into 1D array
        heapq.heapify(m)            # heapify() to turn m into a heap
        
        for i in range(k - 1):      # pop (k - 1) elements so that we can find kth element
            heapq.heappop(m)
            
        return heapq.heappop(m)
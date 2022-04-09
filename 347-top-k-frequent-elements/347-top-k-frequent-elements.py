from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, y in Counter(nums).most_common(k)]
        
        #----------------------------------------------------------
        # ans,y = [],nums[0]
        # a = Counter(nums)
        # while(k):
        #     x = 0
        #     x = a[nums[0]]
        #     for i in a:
        #         if x<=a[i]:
        #             x = a[i]
        #             y = i
        #     ans.append(y)
        #     a[y] = 0
        #     k -= 1
        # return ans
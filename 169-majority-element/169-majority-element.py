#---------------Using algorithm---------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def findCandidate(A):
            maj_index = 0
            count = 1
            for i in range(len(A)):
                if A[maj_index] == A[i]:
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    maj_index = i
                    count = 1
            return A[maj_index]
        
        def isMajority(A, cand):
            count = 0
            for i in range(len(A)):
                if A[i] == cand:
                    count += 1
            if count > len(A)/2:
                return True
            else:
                return False
            
        
        cand = findCandidate(nums)
        if isMajority(nums, cand) == True:
            return cand
        return -1

    #-----------------------------------------------------------------------------------------------
        
#         a = [1]
#         x = nums[0]
#         for i in range(1,len(nums)):
#             if a[-1] == 0:
#                 x = nums[i]
#                 a.append(1)
#             elif x == nums[i]:
#                 a.append(a[-1]+1)
#             else:
#                 a.append(a[-1]-1)
                
#         for i in range(len(a)):
#             c = 0
#             if x == nums[i]:
#                 c += 1
#         if c > len(nums)//2:
#             return x
#         return -1
        
        
        #-------------------------36/43 test cases passed--------------------------------------------
        # a = [1]
        # x = nums[0]
        # for i in range(1,len(nums)):
        #     if a[-1] == 0:
        #         x = nums[i]
        #         a.append(1)
        #     elif x == nums[i]:
        #         a.append(a[-1]+1)
        #     else:
        #         a.append(a[-1]-1)
        # c,z = 0,max(a)
        # for i in a:
        #     if i == z:
        #         c += 1
        # if c == 1:
        #     x = a.index(z)
        # elif c>1:
        #     for i in range(len(a)-1,0,-1):
        #         if a[i] == z:
        #             x = i
        #             break
        # else:
        #     return -1
        # c = 0
        # for i in nums:
        #     if i == nums[x]:
        #         c += 1
        # if c > len(nums)//2:
        #     return nums[x]
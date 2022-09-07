class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            x,flag = 0,0
            for j in range(len(nums2)):
                if(nums1[i]==nums2[j]):
                    x = 1
                elif(x):
                    if(nums1[i]<nums2[j]):
                        nums1[i] = nums2[j]
                        flag = 1
                        break
            if(not flag): nums1[i] = -1
        return nums1
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {} 
        stack = [] 
        for num in nums2:
            while len(stack) and stack[-1] < num:
                nextGreater[stack.pop()] = num
            stack.append(num)
        for idx in range(len(nums1)):
            nums1[idx] = nextGreater.get(nums1[idx], -1)
        return nums1
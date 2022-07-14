class Solution:
    def func(self,idx,a,res):
        if idx == len(a):
            res.append(list(a))
            return
        for i in range(idx,len(a)):
            a[idx],a[i]=a[i],a[idx]
            self.func(idx+1,a,res)
            a[idx],a[i]=a[i],a[idx]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.func(0,nums,res)
        return res
        
        
#-----------------------Approach 2----------------------------
# class Solution:
#     def func(self,a,arr,res,freq):
#         if len(arr) == len(a):
#             res.append(list(arr))
#             return
#         for i in range(len(a)):
#             if (not freq[i]):
#                 arr.append(a[i])
#                 freq[i] = 1
#                 self.func(a,arr,res,freq)
#                 freq[i] = 0
#                 arr.pop()
    
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         freq = [0]*len(nums)
#         self.func(nums,[],res,freq)
#         return res
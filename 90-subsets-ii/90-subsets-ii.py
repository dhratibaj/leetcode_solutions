class Solution:
    def func(self,idx,a,ds,res):
        res.append(list(ds))
        for i in range(idx,len(a)):
            if i!=idx and a[i]==a[i-1]: continue
            ds.append(a[i])
            self.func(i+1,a,ds,res)
            ds.pop()
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.func(0,nums,[],res)
        return res
        
#--------------------------------Brute Force : 15/20 test cases passed-----------------------------------------------
# class Solution:
#     def func(self,idx,a,arr,res):
#         if idx == len(a):
#             if arr not in res:
#                 res.append(list(arr))
#             return
#         arr.append(a[idx])
#         self.func(idx+1,a,arr,res)
#         arr.pop()
#         self.func(idx+1,a,arr,res)
    
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.func(0,nums,[],res)
#         return res
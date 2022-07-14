class Solution:
    def func(self,idx,a,arr,res):
        if idx == len(a):
            res.append(list(arr))
            return
        arr.append(a[idx])
        self.func(idx+1,a,arr,res)
        arr.pop()
        self.func(idx+1,a,arr,res)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.func(0,nums,[],res)
        return res
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if gap == 0: return True
        i = 0
        while i < len(arr):
            if arr[i] == m + i * gap:
                i += 1
            else:
                dis = arr[i] - m
                if dis % gap != 0: return False
                pos = int(dis / gap)
                if arr[pos] == arr[i]: return False
                arr[pos], arr[i] = arr[i], arr[pos]
        return True
        
        # m = min(arr)
        # gap = (max(arr) - m) / (len(arr) - 1)
        # if gap == 0: return True
        # s = set(num - m for num in arr)
        # return len(s) == len(arr) and all(diff % gap == 0 for diff in s)
        
        # arr.sort()
        # d=arr[1]-arr[0]
        # for i in range(1,len(arr)-1):
        #     if d != arr[i+1]-arr[i]:
        #         return False
        # return True
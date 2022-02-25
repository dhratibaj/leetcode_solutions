class Solution:
    def average(self, salary: List[int]) -> float:
        count,n = 0,0
        for i in salary:
            if i!=min(salary) and i!=max(salary):
                count+=(i)
                n+=1
        return count/n
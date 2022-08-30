class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary)/len(salary)
    
        # salary.sort()
        # s = sum(salary)-salary[0]-salary[-1]
        # return s/(len(salary)-2)
        
        #-------------------------------------------
        # count,n = 0,0
        # for i in salary:
        #     if i!=min(salary) and i!=max(salary):
        #         count+=(i)
        #         n+=1
        # return count/n
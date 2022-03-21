class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Check if the input is empty or different length
        if len(tops)!=len(bottoms) or len(tops)==0 or len(bottoms)==0:
            return -1
        else:
            
            total = {tops[0],bottoms[0]} 
            for i in range(1,len(tops)):
                total = total.intersection({tops[i],bottoms[i]})
            
			# If total has lenght of 0 means no common number in all the dominos positions
            if not len(total):
                return -1
            else:
                return(len(tops)-max(tops.count(int(list(total)[0])),bottoms.count(int(list(total)[0]))))
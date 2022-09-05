class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen:
                return False
            elif n == 1:
                return True
            else:
                seen.add(n)
				# h(x): convert int to str -> sum(foreach character in str -> int(character) ^ 2) 
                n = sum([int(x) ** 2 for x in str(n)])
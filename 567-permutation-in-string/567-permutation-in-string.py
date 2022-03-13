class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

        def ch_to_prime(ch):
            return primes[ord(ch)-ord('a')]
    
        if len(s2) < len(s1):
            return False
        
        target_hash = 1
        for ch in s1:
            target_hash *= ch_to_prime(ch)
        
        cur_hash = 1
        for i in range(len(s1)):
            cur_hash *= ch_to_prime(s2[i])
            
        if cur_hash == target_hash:
            return True
        
        p1 = 0
        for p2 in range(len(s1), len(s2)):
            cur_hash //= ch_to_prime(s2[p1])
            cur_hash *= ch_to_prime(s2[p2])
            if cur_hash == target_hash:
                return True
            p1 += 1
            
        return False
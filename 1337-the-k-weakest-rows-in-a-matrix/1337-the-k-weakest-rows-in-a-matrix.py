class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rem, res = k, []
        sold = [sum(row) for row in mat]
        while rem > 0:
            min_ind = min(range(len(sold)), key=sold.__getitem__)
            rem -= 1
            sold[min_ind] = 101
            res.append(min_ind)
        return res
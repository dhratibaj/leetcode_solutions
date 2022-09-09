class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        return ''.join(a+b for a,b in zip_longest(w1,w2,fillvalue=''))
        
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         n,m,i = len(word1),len(word2),0
#         res = ""
#         while(i<n and i<m):
#             res += word1[i]+word2[i]
#             i+=1
#         if(i==n):
#             res += word2[i:]
#         else:
#             res += word1[i:]
#         return res
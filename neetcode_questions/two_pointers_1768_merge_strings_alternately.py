class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = len(word1) -1
        y = len(word2) -1
        final_string=''
        for z in range(max(x,y)+1):
            if z <= min(x,y):
                final_string=final_string+word1[z]+word2[z]
            elif z <= x and y < z:
                final_string = final_string + word1[z]
            elif z <=y  and  x< z  :
                final_string = final_string + word2[z]
        return final_string

# s = Solution()
# word1 = "pqrs"
# word2 = "abc"
# print(s.mergeAlternately(word1,word2))


# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         m = len(word1)
#         n = len(word2)
#         i = 0
#         j = 0
#         result = []
#
#         while i < m or j < n:
#             if i < m:
#                 result += word1[i]
#                 i += 1
#             if j < n:
#                 result += word2[j]
#                 j += 1
#
#         return "".join(result)
#

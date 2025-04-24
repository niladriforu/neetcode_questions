class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        left = 0
        start_position = len(p)
        final_list = []
        for right in range(start_position, len(s)):
            sub_string = s[left:right]
            if sorted(sub_string) == sorted(p):
                final_list.append(left)
            left += 1
            start_position += 1
        return final_list


s= "abab"
p = "ab"
so = Solution()
print(so.findAnagrams(s, p))

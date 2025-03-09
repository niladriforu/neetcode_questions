class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        window = set()
        for right in range(len(s)):
            if s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            length=max(right -left +1 , length)
        return length


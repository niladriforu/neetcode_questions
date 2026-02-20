class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for pos,char in enumerate(s):
            if pos == 0:
                final_word = s[pos+1:]
            else:
                final_word = s[0:pos] + s[pos+1:]
            if final_word == final_word[::-1]:
                return True
        return False

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s,left, right):
            while left < right :
                if s[left] == s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True

        if s == s[::-1]:
            return True
        left = 0
        right = len(s) -1
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return isPalindrome(s,left+1,right) or isPalindrome(s,left,right-1)
        return True

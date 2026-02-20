# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

#Mysolution
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s=re.sub(r'[^a-zA-Z0-9]','',s).lower()
        # formatted_s = [ char for char in s if s.isalnum() ]
        left = 0
        right = len(formatted_s) - 1

        while left < right:
            if formatted_s[left] == formatted_s[right]:
                left+=1
                right-=1
            else:
                return False
        return True

#Mysolution
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = [ char for char in s if s.isalnum() ]
        left = 0
        right = len(formatted_s) - 1

        while left < right:
            if formatted_s[left] == formatted_s[right]:
                left+=1
                right-=1
            else:
                return False
        return True

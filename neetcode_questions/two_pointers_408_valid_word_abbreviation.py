class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        left = 0
        word_list = list(word)
        int_val = ''
        count = 0
        for right in range(len(abbr)):
            if abbr[right].isalpha():
                if count > 0:
                    left +=int(int_val)
                    int_val = ''
                    count = 0
                if abbr[right] == word_list[left]:
                    left+=1
                    continue
                else:
                    return False
            elif abbr[right].isnumeric():
                int_val = int_val + str(abbr[right])
                count +=1
        return True


word = "internationalization"
abbr = "i12iz4a"

s = Solution()
print(s.validWordAbbreviation(word,abbr))
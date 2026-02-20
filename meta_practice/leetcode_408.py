class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        pointer_word, pointer_abbrn = 0, 0
        while pointer_word < len(word) and pointer_abbrn < len(abbr):
            if word[pointer_word] == abbr[pointer_abbrn]:
                pointer_word += 1
                pointer_abbrn += 1
            elif not abbr[pointer_abbrn].isdigit() or abbr[pointer_abbrn] == '0':
                return False
            else:
                skip = 0
                while pointer_abbrn < len(abbr) and abbr[pointer_abbrn].isdigit():
                    skip = skip * 10 + int(abbr[pointer_abbrn])
                    pointer_abbrn += 1
                pointer_word += skip
        return pointer_word == len(word) and pointer_abbrn == len(abbr)



class Solution1:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')
        return s == ''

class Solution2:
    def isValid(self, s: str) -> bool:
        # s = "([{(}])"
        stack = []
        bracket_dict = {
                        ')' : '(',
                        '}' : '{',
                        ']' : '['
                            }
        for c in s:
            if c in bracket_dict:
                if stack and stack[-1] == bracket_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
                '{': '}',
                '[' : ']',
                '(' : ')'
            }
        for c in s:
            if c in m:
                stack.append(c)
            else:
                if stack:
                    opening = stack.pop()
                    if m[opening] != c:
                        return False
                else:
                    return False
        return True if not stack else False
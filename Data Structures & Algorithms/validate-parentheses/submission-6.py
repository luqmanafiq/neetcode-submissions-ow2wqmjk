class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {'{': '}', '[' : ']', '(' : ')'}
        for c in s:
            if c in openToClose:
                stack.append(c)
            else:
                if stack:
                    opening = stack.pop()
                    if openToClose[opening] != c:
                        return False
                else:
                    return False
        return not stack
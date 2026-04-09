class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c not in bracket:
                stack.append(c)
            else:
                if not stack or bracket[c] != stack.pop():
                    return False
        return not stack
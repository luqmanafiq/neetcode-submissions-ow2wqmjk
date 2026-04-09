class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "}": "{", "]":"["}
        for bracket in s:
            if bracket not in hashmap:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop() != hashmap[bracket]:
                        return False
        return not stack
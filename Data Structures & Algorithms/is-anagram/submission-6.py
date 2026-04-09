class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_t=sorted(t)
        sorted_s=sorted(s)
        if sorted_s==sorted_t:
            return True
        return False
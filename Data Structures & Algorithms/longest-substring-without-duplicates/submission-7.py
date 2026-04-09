class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0        
        l, r = 0, 0
        longestLength = 0
        seen = set()
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                longestLength = max(longestLength, r - l + 1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1        
        return longestLength
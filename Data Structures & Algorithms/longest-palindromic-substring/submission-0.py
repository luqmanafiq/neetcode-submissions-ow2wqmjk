class Solution:
    def longestPalindrome(self, s: str) -> str:
        count, start = 0, 0
        max_len = 1
        def helper(l, r):
            nonlocal max_len, start
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = max(max_len, r - l + 1)
                    start = l
                l -= 1
                r += 1
        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
        return s[start: start + max_len]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        max_len, start = 0, 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]): 
                    dp[i][j] = True
                    if max_len < (j - i + 1):
                        start = i
                        max_len = j - i + 1
            
        return s[start : start + max_len]
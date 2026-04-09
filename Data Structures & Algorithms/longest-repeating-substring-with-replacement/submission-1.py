class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen=[0]*26
        longest=0
        l=0
        for r in range(len(s)):
            seen[ord(s[r]) - 65]+=1
            while (r-l+1)-max(seen)>k:
                seen[ord(s[l]) - 65]-=1
                l+=1
            longest = max(longest, r-l+1)
        return longest
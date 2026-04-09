class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        output = l = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            max_freq = max(seen.values())
            if (r - l + 1) - max_freq > k:
                seen[s[l]] -= 1
                l += 1
            output = max(output, r - l + 1)
        return output
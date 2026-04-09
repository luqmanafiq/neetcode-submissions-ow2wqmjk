class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = have = 0
        window={}
        required= Counter(t)
        need = len(required)
        result = ""
        best_len=float('inf')

        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r], 0)
            if s[r] in required and window[s[r]]==required[s[r]]:
                have+=1
                while have == need:
                    if (r - l + 1) < best_len:
                        best_len = r - l + 1
                        result = s[l:r+1]
                    window[s[l]] -= 1
                    if s[l] in required and window[s[l]] < required[s[l]]:
                        have -= 1
                    l += 1
        return result
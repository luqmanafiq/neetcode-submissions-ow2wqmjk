class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        needed_char = Counter(t)
        missing_len = len(t)
        l = i = 0
        min_len = float('inf')
        
        for r in range(len(s)):
            if needed_char[s[r]] > 0:
                missing_len -= 1            
            needed_char[s[r]] -= 1
            
            while missing_len == 0:
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    i = l                
                needed_char[s[l]] += 1                
                if needed_char[s[l]] > 0:
                    missing_len += 1                
                l += 1
        
        return "" if min_len == float('inf') else s[i : i + min_len]
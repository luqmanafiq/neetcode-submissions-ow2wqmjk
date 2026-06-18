class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        if len(piles) == h:
            return max(piles)
        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:                
                result = k
                r = k - 1
            else:
                l = k + 1
            
        return result
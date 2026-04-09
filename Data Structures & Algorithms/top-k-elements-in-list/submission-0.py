class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = defaultdict(int)
        for num in nums:
            seen[num]+=1
        sorted_ = sorted(seen.keys(), key=lambda x:seen[x], reverse=True)[:k]
        return sorted_
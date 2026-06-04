class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        count = Counter(nums)
        if max(count.values()) > 1:
            return True
        return False
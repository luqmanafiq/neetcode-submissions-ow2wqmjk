class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        duplicates = set(nums)
        for i in range(len(nums) + 1):
            if i not in duplicates:
                return i 
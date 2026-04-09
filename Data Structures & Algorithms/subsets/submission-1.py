class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        def backtrack(start, combo):
            subset.append(list(combo))
            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i + 1, combo)
                combo.pop()
        backtrack(0, [])
        return subset
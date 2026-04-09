class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(total, combo, start):
            if total == target:
                output.append(list(combo))
                return
            if target < total:
                return
            for j in range(start, len(nums)):
                combo.append(nums[j])
                backtrack(total + nums[j], combo, j)
                combo.pop()
        backtrack(0, [], 0)
        return output
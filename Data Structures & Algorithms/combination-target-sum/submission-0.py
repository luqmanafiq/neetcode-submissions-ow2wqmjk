class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        def backtrack(remaining, combo, i):
            if remaining == 0:
                output.append(list(combo))
                return
            if remaining < 0:
                return
            for j in range(i, len(nums)):
                if nums[j] > remaining:
                    break
                combo.append(nums[j])
                backtrack(remaining - nums[j], combo, j)
                combo.pop()
        backtrack(target, [], 0)
        return output
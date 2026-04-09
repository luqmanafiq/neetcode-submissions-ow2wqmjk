class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        def backtrack(total, combo, i):
            if total == target:
                output.append(list(combo))
                return
            if total > target:
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                combo.append(nums[j])
                backtrack(total + nums[j], combo, j)
                combo.pop()
        backtrack(0, [], 0)
        return output
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
                
        for i in range(low, len(nums)):
            if nums[i] == 1:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
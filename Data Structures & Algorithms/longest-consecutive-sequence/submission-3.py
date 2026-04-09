class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if nums==[]:return 0
        counter=1
        longest=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] or nums[i]-1 == nums[i-1]:
                counter += 1
                longest=max(longest,counter)
            else:
                counter=1
        return longest
        
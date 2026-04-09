class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i, num in enumerate(nums):
            
            difference = target - num
            if difference in hash:
                return [hash[difference], i]
            hash[num]=i
        return []
        
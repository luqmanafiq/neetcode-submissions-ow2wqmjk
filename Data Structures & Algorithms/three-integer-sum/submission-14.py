class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[i] + nums[l] + nums[r]==0:
                    result.append((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif nums[i] + nums[l] + nums[r]>0:
                    r-=1
                else:
                    l+=1
        return result
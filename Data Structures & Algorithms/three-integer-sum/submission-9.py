class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        n=len(nums)

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                sssum=nums[i] + nums[l] + nums[r]
                if sssum==0:
                    result.append((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                    
                elif sssum>0:
                    r-=1
                else:
                    l+=1
        return result
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater=0
        n=len(heights)
        l,r=0,n-1
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            maxWater=max(maxWater,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxWater
class Solution:
    def trap(self, height: List[int]) -> int:
        area=0
        l,r=0,len(height)-1
        maxright,maxleft=height[r],height[l]
        while l<r:
            if maxleft<maxright:
                l+=1
                maxleft=max(maxleft,height[l])
                area+=maxleft-height[l]
            else:
                r-=1
                maxright=max(maxright,height[r])
                area+=maxright-height[r]
        return area
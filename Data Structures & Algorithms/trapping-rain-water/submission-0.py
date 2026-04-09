class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left,right=0,len(height)-1
        MaxLeft, MaxRight = height[left], height[right]
        area=0

        while left<right:
            if MaxLeft < MaxRight:
                left+=1
                MaxLeft=max(MaxLeft, height[left])
                area+=MaxLeft-height[left]
            else: 
                right-=1
                MaxRight=max(MaxRight, height[right])
                area+=MaxRight-height[right]

        return area
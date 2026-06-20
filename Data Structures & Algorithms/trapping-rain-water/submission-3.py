class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        l_height, r_height = height[l], height[r]
        while l <= r:
            if height[l] < height[r]:
                l_height = max(l_height, height[l])
                area += (l_height - height[l])
                l += 1
            else:
                r_height = max(r_height, height[r])
                area += (r_height - height[r])
                r -= 1
        return area
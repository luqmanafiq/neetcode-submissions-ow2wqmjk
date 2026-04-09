class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return []
        max_win_ele = []
        l = 0
        r = k - 1

        while r < len(nums):
            window = nums[l:r+1]
            max_win_ele.append(max(window))
            l+=1
            r+=1

        return max_win_ele
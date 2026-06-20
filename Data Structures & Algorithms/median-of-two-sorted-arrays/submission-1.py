class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums1) - 1
        while True:
            i = l + (r - l) // 2
            j = ((len(nums1) + len(nums2) + 1) // 2) - (i + 1) - 1

            nums1_left = nums1[i] if i >= 0 else float('-inf')
            nums1_right = nums1[i + 1] if i + 1 < len(nums1) else float('inf')
            nums2_left = nums2[j] if j >= 0 else float('-inf')
            nums2_right = nums2[j + 1] if j + 1 < len(nums2) else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(nums1_left, nums2_left)
                return (min(nums1_right, nums2_right) + max(nums1_left, nums2_left)) / 2.0
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1
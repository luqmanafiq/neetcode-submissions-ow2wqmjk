class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = l + (r - l) // 2
            m = mid // cols
            n = mid % cols
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
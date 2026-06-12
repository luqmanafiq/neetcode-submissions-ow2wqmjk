class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        island_count = 0
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    island_count += 1
        return island_count
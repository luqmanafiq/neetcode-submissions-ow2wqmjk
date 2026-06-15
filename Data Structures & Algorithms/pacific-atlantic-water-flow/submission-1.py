class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic= set()
        pacific = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,prev, visited):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if (r,c) in visited or heights[r][c]<prev:
                return
            visited.add((r,c))
            dfs(r + 1, c, heights[r][c], visited) # Down
            dfs(r - 1, c, heights[r][c], visited) # Up
            dfs(r, c + 1, heights[r][c], visited) # Right
            dfs(r, c - 1, heights[r][c], visited) # Left

        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific) # Left
            dfs(r, cols-1,heights[r][cols-1], atlantic) # Right
        for c in range(cols):
            dfs(rows-1, c, heights[rows-1][c],atlantic) # Bottom
            dfs(0 ,c, heights[0][c],pacific) # Top
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        q = deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()            
                for dr, dc in directions:
                    nr,nc = r + dr,c + dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        return time if fresh == 0 else -1
        
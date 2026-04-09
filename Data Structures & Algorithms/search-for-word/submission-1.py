class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if 0 > r or r >= row or 0 > c or c >= col or word[i] != board[r][c] or (r, c) in visited:
                return False
            visited.add((r, c))
            output = (dfs(r + 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return output

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
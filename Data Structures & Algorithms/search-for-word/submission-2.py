class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        row, col = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if 0 > r or r >= row or 0 > c or c >= col or word[i] != board[r][c]:
                return False
            temp = board[r][c]
            board[r][c] = '#'
            output = (dfs(r + 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c - 1, i + 1))
            board[r][c] = temp
            return output

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
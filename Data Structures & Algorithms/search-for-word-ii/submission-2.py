class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = w

        row, col = len(board), len(board[0])
        output = []
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(r, c, node):
            if not (0 <= r < row and 0 <= c < col):
                return
            temp = board[r][c]
            if temp == '#' or temp not in node.children:
                return
            next_node = node.children[temp]
            if next_node.is_word:
                output.append(next_node.is_word)
                next_node.is_word = None
            board[r][c] = '#'
            for dr, dc in direction:
                dfs(r + dr, c + dc, next_node)
            board[r][c] = temp

        for r in range(row):
            for c in range(col):
                dfs(r, c, root)

        return output
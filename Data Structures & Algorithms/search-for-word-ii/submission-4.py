class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w
        
        rows = len(board)
        cols = len(board[0]) if board else 0
        result = []
        
        def dfs(r, c, node):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            letter = board[r][c]
            if letter == '#' or letter not in node.children:
                return
            
            curr_node = node.children[letter]
            
            if curr_node.word is not None:
                result.append(curr_node.word)
                curr_node.word = None
            
            board[r][c] = '#'
            
            dfs(r - 1, c, curr_node)
            dfs(r + 1, c, curr_node)
            dfs(r, c - 1, curr_node)
            dfs(r, c + 1, curr_node)
            
            board[r][c] = letter
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result
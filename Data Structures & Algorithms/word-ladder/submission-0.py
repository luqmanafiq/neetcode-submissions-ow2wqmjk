class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        unique_words = set(wordList)
        if beginWord in unique_words:
            unique_words.remove(beginWord)
        
        visited = set([beginWord])
        q = deque([(beginWord, 1)])
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    pattern = word[:i] + char + word[i + 1:]
                    if pattern in unique_words and pattern not in visited:
                        visited.add(pattern)
                        q.append((pattern, step + 1))
                        unique_words.remove(pattern)
        return 0
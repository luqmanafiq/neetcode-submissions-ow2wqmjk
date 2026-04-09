class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        unique_words = set()
        for word in words:
            for char in word:
                unique_words.add(char)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
        visited = {char: 0 for char in unique_words}
        order = []

        def dfs(char):
            if visited[char] == 1:
                return False
            if visited[char] == 2:
                return True
            visited[char] = 1
            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False
            visited[char] = 2
            order.append(char)
            return True

        for char in unique_words:
            if visited[char] == 0:
                if not dfs(char):
                    return ""
        
        order.reverse()
        return "".join(order)
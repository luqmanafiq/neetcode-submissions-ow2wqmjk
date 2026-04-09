class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        if not dfs(0, -1):
            return False            
        return n == len(visited)
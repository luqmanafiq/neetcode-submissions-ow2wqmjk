class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[0] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        connected_edges = 0
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    print(neighbor)
        for i in range(n):
            if i not in visited:
                connected_edges += 1
                visited.add(i)
                dfs(i)
        print(graph)
        return connected_edges
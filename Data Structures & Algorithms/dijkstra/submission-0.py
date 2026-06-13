class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i:[] for i in range(n)}
        for u,v,w in edges:
            adj[u].append((v,w))
        distance = {i:float('inf') for i in range(n)}
        distance[src] = 0
        min_heap = [(0, src)]
        while min_heap:
            dist, u = heapq.heappop(min_heap)
            if dist > distance[u]:
                continue
            for v, w in adj[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    heapq.heappush(min_heap, (distance[v],v))
        return {node:(dist if dist != float('inf') else -1) for node, dist in distance.items()}
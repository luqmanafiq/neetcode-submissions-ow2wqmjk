class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}
        for start, end, weight in times:
            adj[start].append((end, weight))
        min_heap = [(0, k)]
        visited = set()
        time = 0
        while min_heap:
            curr_dist, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            time = curr_dist
            for nei, wei in adj[curr_node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (curr_dist + wei, nei))
        return time if len(visited) == n else -1
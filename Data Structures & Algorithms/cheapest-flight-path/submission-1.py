class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, price in flights:
            graph[a].append((b, price))
        
        q = [(0, src, 0)]
        visited = {}
        while q:
            cost, city, stop = heapq.heappop(q)
            if city == dst:
                return cost
            if stop > k:
                continue
            if (city, stop) in visited and visited[(city, stop) <= cost]:
                continue
            visited[(city, stop)] = cost

            for next_city, price in graph[city]:
                new_cost = cost + price
                next_stop = stop + 1
                heapq.heappush(q, (new_cost, next_city, next_stop))
        return -1
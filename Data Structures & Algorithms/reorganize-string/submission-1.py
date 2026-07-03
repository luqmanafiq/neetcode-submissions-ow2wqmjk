class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxheap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(maxheap)
        result = []
        curr_char = ""
        curr_count = 0

        while maxheap:
            cnt, char = heapq.heappop(maxheap)
            result.append(char)
            cnt += 1
            
            if curr_count < 0:
                heapq.heappush(maxheap, [curr_count, curr_char])
            curr_char = char
            curr_count = cnt
            
        output = "".join(result)
        if len(s) != len(output):
            return ""
        return output
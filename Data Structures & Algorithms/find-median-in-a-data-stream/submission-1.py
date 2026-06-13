class MedianFinder:

    def __init__(self):
        self.max_heap = []   # left half  (negate values for max-heap)
        self.min_heap = []   # right half (natural min-heap)

    def addNum(self, num: int) -> None:
        # Step 1: push to max_heap first
        heapq.heappush(self.max_heap, -num)

        # Step 2: balance — max_heap top must be ≤ min_heap top
        if self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Step 3: balance sizes — max_heap can only be 1 larger
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]           # odd total — left has extra
        return (-self.max_heap[0] + self.min_heap[0]) / 2  # even total
        
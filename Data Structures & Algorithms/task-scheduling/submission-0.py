class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        count_max_freq = 0

        max_freq = max(freq.values())
        for freq in freq.values():
            if freq == max_freq:
                count_max_freq += 1 
        min_time = (max_freq - 1) * (n + 1) + count_max_freq
        return max(len(tasks), min_time)
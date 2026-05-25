class TimeMap:

    def __init__(self):
        self.store = {} # { key : (timestamp, value)}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        result = ""
        value = self.store[key]
        l, r = 0, len(value) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if value[mid][0] <= timestamp:
                result = value[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return result
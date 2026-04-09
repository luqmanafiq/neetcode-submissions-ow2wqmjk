class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}
        if timestamp not in self.map:
            self.map[key][timestamp] = []
        self.map[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        seen = 0
        for time in self.map[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.map[key][seen][-1]

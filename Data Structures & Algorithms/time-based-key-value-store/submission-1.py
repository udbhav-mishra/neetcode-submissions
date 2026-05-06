class TimeMap:

    def __init__(self):
        self.hmap = {}       # we can use defaultdict() but I dont want to abuse python too much

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        answer = ""
        values = self.hmap.get(key, [])

        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                answer = values[mid][0]
                left = mid + 1
            else: right = mid - 1
        return answer
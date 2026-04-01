class TimeMap:

    def __init__(self):
        self.key_to_timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timestamps[key].append((timestamp, value))
        # strictly increasing so its always in sorted order no matter what

    def get(self, key: str, timestamp: int) -> str:

        arr = self.key_to_timestamps[key]

        l, r = 0, len(arr)-1
        res = ""
        while l <= r: # stop when left > right

            mid = (l + r) // 2
            time, val = arr[mid]
            if time == timestamp:
                return val
            elif time > timestamp:
                r = mid - 1
            else:
                res = val
                l = mid + 1
        
        return res

        

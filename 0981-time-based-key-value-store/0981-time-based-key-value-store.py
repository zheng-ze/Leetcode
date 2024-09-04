class TimeMap:

    def __init__(self):
        self.dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.dict[key]
        
        if not values:
            return ''
        
        lo, hi = 0, len(values) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            time, value = values[mid]
            
            if timestamp == time:
                return value
            
            if time > timestamp:
                hi = mid - 1
            else:
                lo = mid
        return values[lo][1] if values[lo][0] <= timestamp else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
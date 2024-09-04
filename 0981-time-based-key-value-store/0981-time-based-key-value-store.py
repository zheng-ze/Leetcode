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
        maxValue = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            time, value = values[mid]
            
            if timestamp == time:
                return value
            
            if time < timestamp:
                maxValue = value
                lo = mid + 1
            else:
                hi = mid - 1
                
        return maxValue


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
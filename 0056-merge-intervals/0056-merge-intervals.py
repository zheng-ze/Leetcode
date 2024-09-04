class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        
        if length <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        
        curr = intervals[0]
        out = [curr]
        
        for interval in intervals:
            if interval[0] <= curr[1]:
                curr[1] = max(interval[1], curr[1])
            else:
                curr = interval
                out.append(curr)
        
        return out
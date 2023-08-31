class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Create the ranges
        for i in range(len(ranges)):
            ranges[i] = (i - ranges[i], i + ranges[i])
        # Sort ranges by their start point then their end point
        ranges.sort(key=lambda x: x[0])
        
        print(ranges)
        
        # Greedily take in ranges as long as they their start point is within the current range.
        # However, only include it in count after reaching a point where start point is lesser than
        # start of current range. This is so that we can get the optimal range that increases the
        # the range the most.
        start = 0
        end = 0
        count = 0
        i = 0
        while start < n:
            while i < len(ranges) and ranges[i][0] <= start:
                end = max(end, ranges[i][1])
                i += 1
                            
            if start == end:
                return -1
            
            count += 1
            start = end

        return count
            
        
        
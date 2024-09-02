class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        
        i, length = 0, len(intervals)
        newStart, newEnd = newInterval
        
        # Add intervals that are unaffected
        while i < length:
            interval = intervals[i]
            
            if interval[1] >= newStart:
                break
            
            output.append(interval)
            i += 1
        
        # Merge and add remaining intervals
        while i < length:
            # No longer affected
            if intervals[i][0] > newEnd:
                break
            start, end = intervals[i]
            newStart = min(newStart, start)
            newEnd = max(newEnd, end)
            i += 1
        
        output.append([newStart, newEnd])
        output.extend(intervals[i:])
        
        return output
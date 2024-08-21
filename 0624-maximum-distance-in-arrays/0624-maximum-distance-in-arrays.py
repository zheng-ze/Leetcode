class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = 10000
        largest = -10000
        maxDiff = 0
        
        for arr in arrays:
            currSmall, currBig = arr[0], arr[-1]
            maxDiff = max(maxDiff, currBig - smallest, largest - currSmall)
            smallest = min(smallest, currSmall)
            largest = max(largest, currBig)
        
        return maxDiff
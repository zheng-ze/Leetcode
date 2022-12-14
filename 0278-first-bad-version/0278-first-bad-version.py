# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower = 0
        upper = n
        
        while lower < upper:
            mid = lower + (upper - lower) // 2
            
            if isBadVersion(mid):
                upper = mid
            else:
                lower = mid + 1
            print(mid, lower, upper)

        
        return lower

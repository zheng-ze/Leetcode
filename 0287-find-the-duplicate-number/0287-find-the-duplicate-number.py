class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            count = sum(1 for _ in filter(lambda num: num <= mid, nums))
            
            if count > mid:
                hi = mid
            else:
                lo = mid + 1
                
        return lo
             
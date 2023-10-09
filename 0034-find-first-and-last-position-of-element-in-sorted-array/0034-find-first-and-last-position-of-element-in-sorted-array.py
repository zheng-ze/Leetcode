class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        if not length:
            return [-1, -1]
        
        if length == 1:
            return [-1, -1] if nums[0] != target else [0, 0]
        
        lo = 0
        hi = length - 1
        found = False
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                found = True
                hi = mid - 1
        
        if not found:
            return [-1, -1]
        
        hi = lo
        
        while hi < length and nums[hi] == target:
            hi += 1
        
        return [lo, hi - 1]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        
        length = len(nums)
        lo, hi = 0, length - 1
        
        # Look for pivot
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        if lo == 0 or target < nums[0]:
            hi = length - 1
        else:
            hi = lo - 1
            lo = 0
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1
        
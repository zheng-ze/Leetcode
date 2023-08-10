class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #find the pivot
        lo, hi = 0, len(nums) - 1

        while lo <= hi:            
            while lo < hi and nums[lo] == nums[lo + 1]:
                lo += 1
            while hi > lo and nums[hi] == nums[hi - 1]:
                hi -= 1
            
            mid = (lo + hi) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[lo] <= nums[mid]:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid -1
                
            
            
        return False
                
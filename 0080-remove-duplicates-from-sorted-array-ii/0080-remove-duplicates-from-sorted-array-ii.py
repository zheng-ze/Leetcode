class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        pos = 0
        i = 0
        
        # Each iteration of outer loop will handle a new number.
        # All duplicates are resolved in inner loop.
        while i < len(nums):
            nums[pos] = nums[i]
            pos += 1
            
            while i < len(nums) - 2 and nums[i] == nums[i + 2]:
                i += 1
            
            i += 1
        
        return pos
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = decrease = False
        
        for i in range(len(nums) - 1):
            if not increase and nums[i] < nums[i + 1]:
                increase = True
                continue
            if not decrease and nums[i] > nums[i + 1]:
                decrease = True
                continue
        
        return not (increase and decrease)
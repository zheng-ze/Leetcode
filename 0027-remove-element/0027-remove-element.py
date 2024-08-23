from collections import deque 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fillIndex = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[fillIndex] = nums[i]
                fillIndex += 1
        
        return fillIndex
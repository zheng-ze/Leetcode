from collections import deque 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removedPositions = deque([])
        removed = 0
        for i in range(len(nums)):
            if nums[i] == val:
                removedPositions.append(i)
                removed += 1
                continue
            
            if len(removedPositions) > 0:
                fillPos = removedPositions[0]
                removedPositions.popleft()
                nums[fillPos] = nums[i]
                removedPositions.append(i)
                
        return len(nums) - removed
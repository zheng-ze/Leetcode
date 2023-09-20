class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Idea to find the longest subarray that adds up to sum - x
        target = sum(nums) - x
        if target == 0: # x == sum. Therefore need all numbers
            return len(nums)
        
        if target < 0:
            return -1
        
        currSum = 0
        i = 0
        j = 0
        length = len(nums)
        longest = -1
        
        while j < length or (currSum > target and i < length):
            # Ensure that each outer loop will have currSum >= target
            while j < length and currSum < target:
                currSum += nums[j]
                j += 1
            
            if currSum == target:
                longest = max(longest, j - i)
            currSum -= nums[i]
            i += 1
        
        if currSum == target:
            longest = max(longest, j - i)
        
        return length - longest if longest != -1 else -1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        curr = 0
        
        for num in nums:
            curr += num
            maxSum = max(maxSum, curr)
            curr = max(0, curr)
            
        
        return maxSum
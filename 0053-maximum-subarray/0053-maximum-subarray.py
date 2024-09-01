class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        maxPrevSum = 0
        
        for num in nums:
            maxSum = max(maxSum, num + maxPrevSum)
            maxPrevSum = max(0, maxPrevSum + num)
        
        return maxSum
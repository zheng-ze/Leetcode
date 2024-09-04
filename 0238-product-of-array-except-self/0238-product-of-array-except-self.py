class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        
        length = len(nums)
        out = [1 for i in range(length)]
        
        for i in range(1, length):
            out[i] = out[i - 1] * nums[i - 1]
        
        right = 1
        for i in range(length - 2, -1, -1):
            right *= nums[i + 1]
            out[i] *= right
        
        return out
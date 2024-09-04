class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        
        length = len(nums)
        out = [1 for i in range(length)]
        
        for i in range(1, length):
            out[i] = out[i - 1] * nums[i - 1]
        
        for i in range(length - 2, 0, -1):
            out[0] *= nums[i + 1]
            out[i] *= out[0]
        out[0] *= nums[1]
        
        return out
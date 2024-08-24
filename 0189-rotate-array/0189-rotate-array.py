class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) < 2:
            return
        length = len(nums)
        k = k % length
        
        nums[0:length - k] = nums[0:length - k][::-1]
        nums[length - k:length] = nums[length - k:length][::-1]
        nums[:] = nums[::-1]

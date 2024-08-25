class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            
            if complement in mem:
                return [i, mem[complement]]
            
            mem[num] = i
        return [0, 0]
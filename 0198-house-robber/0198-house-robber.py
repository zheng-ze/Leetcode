class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1 for i in range(len(nums))]
        def execute(houses, index):
            if index < 0:
                return 0
            if mem[index] != -1:
                return mem[index]
            
            mem[index] = max(execute(houses, index - 2) + houses[index], execute(houses, index - 1))
            
            return mem[index]
        
        return execute(nums, len(nums) - 1)
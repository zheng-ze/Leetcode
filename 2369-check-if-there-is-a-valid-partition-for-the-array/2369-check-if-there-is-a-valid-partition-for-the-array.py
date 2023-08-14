class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # Represents validity for prevIndex - 2, prevIndex - 1 and prevIndex
        dp = [True, False, nums[0] == nums[1]]
        
        for i in range(2, len(nums)):
            valid = False
            
            # If curr and prev are equal and if prev is valid, it is possible to partition valid subarrays
            if not valid and dp[1] and nums[i] == nums[i - 1]:
                valid = True
            
            if not valid and dp[0] and (nums[i] == nums[i - 1] == nums[i - 2] \
                                        or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2):
                valid = True
            
            dp[:] = [dp[1], dp[2], valid]
        
        return dp[2]
            
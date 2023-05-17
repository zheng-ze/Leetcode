class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Key idea: Sign only changes when multiplied by negative.
        # Always 0 when multiplied by 0
        sign = 1
        
        for num in nums:
            if num == 0:
                return 0
            
            if num < 0:
                sign *= -1
        
        return sign
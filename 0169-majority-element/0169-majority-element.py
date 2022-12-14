class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
        maximum = None
        count = 0
        for num in nums:
            if count == 0:
                maximum = num
                count += 1
            elif num == maximum:
                count += 1
            else:
                count -= 1
        
        return maximum
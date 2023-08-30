class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        Idea to go from back to front. Make each subsequent element the same or lesser than
        the element on the right.
        """
        length = len(nums)
        if length <= 1:
            return 0
        
        i = length - 2
        prev = nums[i + 1]
        count = 0
        
        for i in range(length - 1, -1, -1):
            print(i)
            curr = nums[i]
            
            splitCount = curr // prev

            if curr % prev != 0:
                splitCount += 1
                prev = curr // splitCount

            count += splitCount - 1
                
        return count
                
            
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        out = []
        nums.sort()
        
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = length - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    while j < length and nums[j] == nums[j - 1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1
                elif total > 0:
                    k -= 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < length and nums[j] == nums[j - 1]:
                        j += 1
        
        return out
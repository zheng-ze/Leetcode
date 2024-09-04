class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        
        def dfs(nums, p, out):
            if not nums:
                out.append(p)
                return
            for num in nums:
                dfs(nums.difference(set([num])), p + [num], out)
        out = []
        dfs(nums, [], out)
        return out
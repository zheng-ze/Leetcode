class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        higher = len(nums) - 1

        while lower <= higher:
            mid = lower + (higher - lower) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                lower = mid + 1
            if target < nums[mid]:
                higher = mid - 1

        return -1
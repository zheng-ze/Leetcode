class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums).values()
        for c in count:
            if c >= 2:
                return True
        return False
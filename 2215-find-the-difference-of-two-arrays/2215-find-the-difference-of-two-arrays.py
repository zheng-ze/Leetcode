class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        present1 = set(nums1)
        present2 = set(nums2)
        
        return [ present1 - present2, present2 - present1 ]
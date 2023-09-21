class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        midIndex = (l1 + l2) // 2 + 1
        
        mid1 = mid2 = 0
        i = j = 0
        
        while i + j < midIndex:
            mid2 = mid1
            
            if j == l2 or (i != l1 and nums1[i] <= nums2[j]):
                mid1 = nums1[i]
                i += 1
            else:
                mid1 = nums2[j]
                j += 1
        
        return (mid1 + mid2) / 2 if (l1 + l2) % 2 == 0 else mid1
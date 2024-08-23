class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len1 = len(nums1)
        
        if n == 0:
            return
        
        if len1 == n:
            for i in range(len1):
                nums1[i] = nums2[i]
        
        
        fillPt = len1 - 1
        pt1 = m - 1
        pt2 = n - 1
            
        while fillPt >= 0:
            if pt1 < 0 or nums2[pt2] >= nums1[pt1] and pt2 >= 0:
                nums1[fillPt] = nums2[pt2]
                pt2 -= 1
            else:
                nums1[fillPt] = nums1[pt1]
                pt1 -= 1
            
            fillPt -= 1        
            
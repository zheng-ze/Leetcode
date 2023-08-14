import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums[:k]
        heapq.heapify(q)
                
        for num in nums[k:]:
            if num > q[0]:
                heapq.heapreplace(q, num)
        
        return q[0]
        
        
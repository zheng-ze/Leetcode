import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        total = 0
        
        for pile in piles:
            total += pile
            heapq.heappush(heap, -1 * pile)
        
        while (k > 0):
            temp = -1 * heapq.heappop(heap)
            total -= temp // 2
            heapq.heappush(heap, -1 * (temp - temp // 2))
            k -= 1
        
        return total
            
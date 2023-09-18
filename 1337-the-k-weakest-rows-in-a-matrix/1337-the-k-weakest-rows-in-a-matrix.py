class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest = []
        heapq.heapify(weakest)
        i = 0
        
        # Initialise the pq with k elements
        while i < k:
            heapq.heappush(weakest, (-sum(mat[i]), -i))
            i += 1
        
        # Keep the weakest k elements
        while i < len(mat):
            if -sum(mat[i]) > weakest[0][0]:
                heapq.heapreplace(weakest, (-sum(mat[i]), -i))
            i += 1
            
        return [-row[1] for row in sorted(weakest, key=lambda x: (-x[0], -x[1]))]
            
            
            
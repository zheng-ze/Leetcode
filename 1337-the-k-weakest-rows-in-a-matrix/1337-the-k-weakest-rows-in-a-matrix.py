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
            print(weakest)
            if -sum(mat[i]) > weakest[0][0]:
                heapq.heapreplace(weakest, (-sum(mat[i]), -i))
            i += 1
        
        # Sort by strength then by index
        def cmp(x, y):
            if x[0] == y[0]:
                return y[1] - x[1]
            return y[0] - x[0]
            
        weakest = sorted(weakest, key=functools.cmp_to_key(cmp))
        return [-row[1] for row in weakest]
            
            
            
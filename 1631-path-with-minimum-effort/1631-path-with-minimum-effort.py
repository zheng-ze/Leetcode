class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows = len(heights)
        cols = len(heights[0])
        
        if rows == 1 and cols == 1:
            return 0
        
        q = []
        heapq.heapify(q)
        heapq.heappush(q, (0, (0, 0)))
        visited = [[False for c in range(cols)] for r in range(rows)]
        
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        while q:
            (effort, (currX, currY)) = heapq.heappop(q)
            
            if visited[currX][currY]:
                continue
                
            visited[currX][currY] = True
            
            if currX == rows - 1 and currY == cols - 1:
                return effort
            
            for d in dirs:
                newX = currX + d[0]
                newY = currY + d[1]
                if newX >= rows or newX < 0 or newY >= cols or newY < 0 or visited[newX][newY]:
                    continue
                    
                newEffort = max(effort, abs(heights[currX][currY] - heights[newX][newY]))
                heapq.heappush(q, (newEffort, (newX, newY)))
        
        return -1 # Should not reach here
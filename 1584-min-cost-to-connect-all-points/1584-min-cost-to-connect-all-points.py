class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        
        if length <= 1:
            return 0
        
        visited = [False for i in range(length)]
        q = []
        heapq.heapify(q)
        numConnected = 0
        i = 0
        out = 0
        
        while numConnected < length - 1 :
            visited[i] = True
            
            for j in range(length):
                if not visited[j]:
                    d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(q, (d, j))
            while q and visited[q[0][1]]:
                heapq.heappop(q)
            out += q[0][0]
            i = heapq.heappop(q)[1]
            numConnected += 1
            
        return out
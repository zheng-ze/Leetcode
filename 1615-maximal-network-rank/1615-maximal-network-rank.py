class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if n == 2:
            return len(roads)
        roadCounts = [0] * n
        connected = [[False for _ in range(n)] for _ in range(n)]
        
        for road in roads:
            roadCounts[road[0]] += 1
            roadCounts[road[1]] += 1
            connected[road[0]][road[1]] = True
            connected[road[1]][road[0]] = True
        
        out = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                out = max(out, roadCounts[i] + roadCounts[j] - (1 if connected[i][j] else 0))
            
        
        return out
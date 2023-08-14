class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0 for c in range(cols)] for r in range(rows)]
        
        paths[0][0] = 1
        
        for r in range(rows):
            for c in range(cols):
                if r + 1 < rows and obstacleGrid[r + 1][c] == 0:
                    paths[r + 1][c] += paths[r][c]
                
                if c + 1 < cols and obstacleGrid[r][c + 1] == 0:
                    paths[r][c + 1] += paths[r][c]
        
        return paths[rows - 1][cols - 1]
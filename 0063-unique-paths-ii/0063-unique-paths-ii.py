class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * cols
        currRow = [0] * cols
        
        prevRow[0] = 1
        
        for r in range(rows):
            currRow[0] = 0 if obstacleGrid[r][0] == 1 else prevRow[0]
            for c in range(1, cols):
                currRow[c] = 0 if obstacleGrid[r][c] == 1 else prevRow[c] + currRow[c - 1]
            prevRow[:] = currRow
        
        return currRow[cols - 1]
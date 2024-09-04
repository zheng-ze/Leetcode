class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lenx, leny = len(grid), len(grid[0])
        
        def dfs(i, j, grid):
            if i < 0 or i >= lenx or j < 0 or j >= leny or grid[i][j] != "1":
                return
            
            grid[i][j] = "0"    
            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)
            dfs(i, j - 1, grid)
            dfs(i, j + 1, grid)
             
        count = 0
        for i in range(lenx):
            for j in range(leny):
                if grid[i][j] != "1":
                    continue
                
                count += 1
                dfs(i, j, grid)
        
        return count
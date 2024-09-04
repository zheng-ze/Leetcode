class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        lenx, leny = len(grid), len(grid[0])
        
        def step(grid, rottens):
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            newRottens = []
            
            for (i, j) in rottens:
                for (dx, dy) in dirs:
                    newi = i + dx
                    newj = j + dy
                    
                    if newi < 0 or newi >= lenx or newj < 0 or newj >= leny or grid[newi][newj] != 1:
                        continue
                    
                    grid[newi][newj] = 2
                    newRottens.append([newi, newj])
            
            return newRottens
        
        rottens = []
        numFresh = 0
        
        for i in range(lenx):
            for j in range(leny):
                if grid[i][j] == 1:
                    numFresh += 1
                if grid[i][j] == 2:
                    rottens.append([i, j])
        
        if numFresh == 0:
            return 0
        
        time = 0
        while numFresh > 0 and rottens:
            rottens = step(grid, rottens)
            time += 1
            
            numFresh -= len(rottens)
        
        return time if numFresh == 0 else -1
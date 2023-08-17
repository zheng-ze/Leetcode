class Solution:
    def __init__(self):
        self.dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        out = [[-1 for c in range(col)] for r in range(row)]
        
        q = deque([])
        
        # Get all 0 and initialise them as starting points
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    out[r][c] = 0
                    q.append((r, c))
        
        # Solve for all distance 0, then 1, 2...
        # Hence, each new unsolved neighbour will be 1 unit further away from a 0
        while q:
            r, c = q.popleft()
            
            for (dr, dc) in self.dir:
                newr = r + dr
                newc = c + dc
                
                if newr < 0 or newr >= row or newc < 0 or newc >= col:
                    continue
                
                if mat[newr][newc] == 0 or out[newr][newc] != -1:
                    continue
                
                out[newr][newc] = out[r][c] + 1
                q.append((newr, newc))
        
        return out
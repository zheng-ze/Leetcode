class Solution:
    def __init__(self):
        self.dp = [[1]] # Memoise to reduce repeated computation
    def generate(self, numRows: int) -> List[List[int]]:
        # If result is already memoised, just return it.
        if len(self.dp) >= numRows:
            return self.dp[:numRows]
        
        # If previous row not computed yet, compute it first.
        if len(self.dp) < numRows - 1:
            self.generate(numRows - 1)
        
        # Compute current row based on previous row
        self.dp.append([1])
        
        # Compute middle
        for i in range(1, numRows - 1):
            self.dp[numRows - 1].append(sum(self.dp[numRows - 2][i - 1: i +1]))
        
        self.dp[numRows - 1].append(1)
        
        return self.dp
        
            
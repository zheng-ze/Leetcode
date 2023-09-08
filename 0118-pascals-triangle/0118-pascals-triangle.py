class Solution:
    def __init__(self):
        self.dp = [[1]]
    def generate(self, numRows: int) -> List[List[int]]:
        if len(self.dp) >= numRows:
            return self.dp[:numRows]
        
        if len(self.dp) < numRows - 1:
            self.generate(numRows - 1)

        row = [1]

        for i in range(1, numRows - 1):
            row.append(sum(self.dp[numRows - 2][i - 1: i +1]))
        
        row.append(1)
        self.dp.append(row)
        
        return self.dp
        
            
class Solution:
    def __init__(self):
        self.dp = [[1]]
    def generate(self, numRows: int) -> List[List[int]]:
        if len(self.dp) >= numRows:
            return self.dp[:numRows]
        
        if len(self.dp) < numRows - 1:
            self.generate(numRows - 1)

        self.dp.append([1])

        for i in range(1, numRows - 1):
            self.dp[numRows - 1].append(sum(self.dp[numRows - 2][i - 1: i +1]))
        
        self.dp[numRows - 1].append(1)
        
        return self.dp
        
            
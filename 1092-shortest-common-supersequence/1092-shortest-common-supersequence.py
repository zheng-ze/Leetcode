class Solution:
    
    
    
    def shortestCommonSupersequence(self, x: str, y: str) -> str:
        def LCS(x: str, y: str) -> str:
            len1, len2 = len(x), len(y)

            if len1 == 0:
                return y
            if len2 == 0:
                return x

            # Find LCS first -> LCS will allow us to remove letters thereby shortening the string
            dp = [["" for _ in range(len2 + 1)] for _ in range(len1 + 1)]

            for i in range(1, len1 + 1):
                for j in range(1, len2 + 1):
                    if x[i - 1] == y[j - 1]:
                        subsequence = dp[i - 1][j - 1]
                        dp[i][j] = subsequence + x[i - 1]
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], key=len)

            # No LCS -> No way to reduce length -> just combine
            return dp[len1][len2]
            
        out = ""
        i = j = 0
        for c in LCS(x, y):
            while x[i] != c:
                out += x[i]
                i += 1
            while y[j] != c:
                out += y[j]
                j += 1
            
            out += c
            i += 1
            j += 1
        
        return out + x[i:] + y[j:]

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)
        length = len(s)
        dp = [0 for i in range(length + 1)]
        
        for i in range(1, length + 1):
            dp[i] = dp[i - 1] + 1
            
            for j in range(i - 1, -1, -1):
                if s[j:i] in d:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[length]
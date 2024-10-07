class Solution:
    def shortestCommonSupersequence(self, x: str, y: str) -> str:
        len1, len2 = len(x), len(y)

        if len1 == 0:
            return y
        if len2 == 0:
            return x

        # Find LCS first -> LCS will allow us to remove letters thereby shortening the string
        dp = [[(0, "") for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = (0, "")
        for j in range(len2 + 1):
            dp[0][j] = (0, "")

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if x[i - 1] == y[j - 1]:
                    length, subsequence = dp[i - 1][j - 1]
                    dp[i][j] = (length + 1, subsequence + x[i - 1])
                else:
                    dp[i][j] = dp[i][j - 1] if dp[i][j - 1] >= dp[i - 1][j] else dp[i - 1][j]

        # No LCS -> No way to reduce length -> just combine
        length, LCS = dp[len1][len2]
        if length == 0:
            return x + y

        # Same word
        if length == len1 == len2:
            return (x)

        # Use LCS to break strings into chunks.
        # Combine chunks to from Shortest Super Sequence
        chunks1 = ["" for _ in range(length + 1)]
        chunks2 = ["" for _ in range(length + 1)]

        i = length - 1
        j = k = len1 - 1
        while i >= 0 and j >= 0:
            while j >= 0 and x[j] != LCS[i]:
                j -= 1
            chunks1[i + 1] = x[j + 1: k + 1]
            j -= 1
            i -= 1
            k = j

        chunks1[0] = x[:k + 1]

        i = length - 1
        j = k = len2 - 1
        while i >= 0 and j >= 0:
            while j >= 0 and y[j] != LCS[i]:
                j -= 1
            chunks2[i + 1] = y[j + 1: k + 1]
            j -= 1
            i -= 1
            k = j
        chunks2[0] = y[:k + 1]

        combined = list(map(lambda x: x[0] + x[1], zip(chunks1, chunks2)))
        out = ""
        for i in range(length):
            out += combined[i] + LCS[i]
        out += combined[-1]

        return out

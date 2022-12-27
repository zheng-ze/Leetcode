class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        start = 0
        maximum = 0
        for i in range(len(s)):
            c = s[i]
            if c in chars and start <= chars[c]:
                start = chars[c] + 1
            else:
                maximum = max(maximum, i - start + 1)

            chars[c] = i

        return maximum
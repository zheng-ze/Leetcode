class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        length = 200
        for s in strs:
            length = min(length, len(s))
        for i in range(length):
            c = ""
            for s in strs:
                if c == "":
                    c = s[i]
                    output += c
                elif c != s[i]:
                    return output[:-1]
        
        return output
                
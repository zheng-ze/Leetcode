class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        seen = set()
        list_s = s.split(" ")
        if len(list_s) != len(pattern):
            return False
        for i in range(len(list_s)):
            if pattern[i] not in dict and list_s[i] not in seen:
                dict[pattern[i]] = list_s[i]
                seen.add(list_s[i])
            elif (list_s[i] in seen and pattern[i] not in dict) or dict[pattern[i]] != list_s[i]:
                return False
        
        return True
            
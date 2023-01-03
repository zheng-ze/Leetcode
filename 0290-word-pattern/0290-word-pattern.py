class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterntos = {}
        stopattern = {}
        list_s = s.split(" ")
        if len(list_s) != len(pattern):
            return False
        for i in range(len(list_s)):
            if pattern[i] not in patterntos:
                patterntos[pattern[i]] = list_s[i]
            elif patterntos[pattern[i]] != list_s[i]:
                return False
            if list_s[i] not in stopattern:
                stopattern[list_s[i]] = pattern[i]
            elif stopattern[list_s[i]] != pattern[i]:
                return False
        
        return True
            
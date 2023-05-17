import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Checks if there is a gcd
        if (str1 + str2 != str2 + str1):
            return ""
        
        # Gets length of gcd and gets gcd
        lengcd = math.gcd(len(str1), len(str2))    
        return str1[:lengcd] 
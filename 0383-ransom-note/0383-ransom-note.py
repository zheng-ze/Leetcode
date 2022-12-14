class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote).items()
        mag = Counter(magazine)
        
        for item, num in ransom:
            if not mag[item] or mag[item] < num:
                return False
        
        return True
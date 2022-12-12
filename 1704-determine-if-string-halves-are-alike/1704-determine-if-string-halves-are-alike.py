class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)
        print(s[:round((length)/ 2)])
        left = Counter(s[:round((length) / 2)])
        right = Counter(s[round((length) / 2):])
        leftsum = 0
        rightsum = 0
        vowels = ["a", "e", "i", "o", "u", "A", 'E', 'I', 'O', 'U']
        for vowel in vowels:
            leftsum += left[vowel]
            rightsum += right[vowel]
        
        return leftsum == rightsum
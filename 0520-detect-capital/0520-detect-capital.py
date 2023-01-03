class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for c in word:
            if c.isupper():
                count += 1
        if count == 1 and word[0].isupper():
            return True
        return count == 0 or count == len(word)
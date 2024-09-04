class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        head = self.trie
        for c in word:
            if c not in head:
                head[c] = {}
            head = head[c]
        head["word"] = True

    def search(self, word: str) -> bool:
        head = self.trie
        for c in word:
            if c not in head:
                return False
            head = head[c]
        
        return head["word"] if "word" in head else False
        

    def startsWith(self, prefix: str) -> bool:
        head = self.trie
        for c in prefix:
            if c not in head:
                return False
            head = head[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
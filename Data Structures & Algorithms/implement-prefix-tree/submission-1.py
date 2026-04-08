class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        level = self.root
        for char in word:
            if char not in level:
                level[char] = {}
            level = level[char]
        level["word"] = True


    def search(self, word: str) -> bool:
        level = self.root
        for char in word:
            if char not in level:
                return False
            level = level[char]
        return level.get("word", False)
        

    def startsWith(self, prefix: str) -> bool:
        level = self.root
        for char in prefix:
            if char not in level:
                return False
            level = level[char]
        return True
        
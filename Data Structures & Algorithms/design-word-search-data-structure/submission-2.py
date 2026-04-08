class WordDictionary:
    # trie + dfs

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        level = self.root
        for char in word:
            if char not in level:
                level[char] = {}
            level = level[char]
        level["word"] = True


    def search(self, word: str) -> bool:
        # use dfs
        def dfs(level, word):
            print(level, word)
            for i, char in enumerate(word):
                if char == ".":
                    for key in level:
                        if key != "word":
                            if dfs(level[key], word[i+1:]):
                                return True
                    return False
                else:
                    if char not in level:
                        return False
                    level = level[char]
            return level.get("word", False)
        return dfs(self.root, word)
        
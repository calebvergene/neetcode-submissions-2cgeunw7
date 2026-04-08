class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs to track number of transformations
        # pretty easy, just see which words you are 1 step away from and then add those to queue if not visited

        visited = set()
        
        # what is the fastest way to compare words?
        # len(wordList) x n
        # or could do 26 x n! so, iterate through alphabet and check each letter in spot 

        wordList = set(wordList)
        
        q = collections.deque()
        q.append(beginWord)
        step = 1
        while q:
            step += 1
            for _ in range(len(q)):
                word = q.popleft()
                # check for neighbor words by replacing letters
                a = ord('a')
                for c in range(len(word)):
                    for l in range(26):
                        possible_word = word[:c] + chr(a+l) + word[c+1:]
                        # valid word!
                        if possible_word in wordList and possible_word not in visited:
                            # found target
                            if possible_word == endWord:
                                return step
                            visited.add(possible_word)
                            q.append(possible_word)
        return 0




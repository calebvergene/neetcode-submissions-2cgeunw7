class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_anagrams = {}
        for word in strs:
            hash_word = {}
            for char in word:
                hash_word[char] = hash_word.get(char, 0) + 1
            hash_word = tuple(sorted((hash_word.items())))
            if hash_word in hash_anagrams:
                hash_anagrams[hash_word].append(word)
            else:
                hash_anagrams[hash_word] = [word]
        return list(hash_anagrams.values())

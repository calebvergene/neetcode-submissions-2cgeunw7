class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs, hasht = {}, {}

        for char in s:
            hashs[char] = hashs.get(char, 0) + 1
        for char in t:
            hasht[char] = hasht.get(char, 0) + 1

        if hashs == hasht:
            return True
        return False
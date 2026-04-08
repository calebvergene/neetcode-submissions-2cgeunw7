class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for char in range(len(s)):
            hashS[s[char]] = 1 + hashS.get(s[char], 0)
            hashT[t[char]] = 1 + hashT.get(t[char], 0)

        for char in set(s):
            if hashS[char] != hashT.get(char, 0):
                return False
        return True

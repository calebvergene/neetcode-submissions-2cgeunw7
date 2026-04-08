class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## check if they are different lengths
        ## if they are, then they are not anagrams
        if len(s) != len(t):
            return False
        
        ## count the frequency of each letter of each word
        hasht = {}
        hashs = {}
        for letter in s:
            hashs[letter] = hashs.get(letter, 0) + 1
        for letter in t:
            hasht[letter] = hasht.get(letter, 0) + 1
        
        if hashs == hasht:
            return True
        return False
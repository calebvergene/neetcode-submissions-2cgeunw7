class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # so, i need to make frequency has of s1 and of the window in s2
        # if they equal each other, then return true

        if len(s2) < len(s1):
            return False

        hash1 = defaultdict(int)
        for letter in s1:
            hash1[letter] += 1
        
        # get hash for first letters in s2
        l,r = 0, 0 
        hash2 = defaultdict(int)
        for r in range(len(s1)):
            hash2[s2[r]] += 1
        
        # now, increment this window through the string
        while (True):

            if hash2 == hash1:
                return True

            print(dict(hash2), dict(hash1))
            
            r += 1
            if r >= len(s2):
                return False 
            hash2[s2[r]] += 1
            hash2[s2[l]] -= 1
            if hash2[s2[l]] == 0:
                del hash2[s2[l]]
            l += 1

        return False
        
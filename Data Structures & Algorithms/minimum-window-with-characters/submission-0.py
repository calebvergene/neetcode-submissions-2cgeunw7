class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sublen = float('inf')
        indexes = (0,0)
        # have a hashmap storing frequency of needed chars in t
        thash = {}
        for char in t:
            thash[char] = thash.get(char, 0) + 1
        shash = {}

        # so first i need to make sure every char in t is atleast in the substring
        # keep a set at the beginning to track the first subtring with all needed t chars
        tset = set(t)

        # r will always be moving forward.
        # l will only move forward if shash[s[l]] > thash[s[l]] and tset is empty,
        # as this ensures you have a filled substring
        r, l = 0, 0
        while r < len(s):
            if s[r] in t:
                shash[s[r]] = shash.get(s[r], 0) + 1
                # delete from set if enough chars in substring. we have reached the amount needed
                if s[r] in tset and shash[s[r]] == thash[s[r]]:
                    tset.remove(s[r])
                # to move l forward, need to have over the amount of char needed in the substring 
                if len(tset) == 0:
                    # disregard char because not needed or have abundance of it
                    while s[l] not in thash or shash[s[l]] > thash[s[l]]:
                        if s[l] in thash: shash[s[l]] -= 1
                        l += 1
                # now update min substring if all chars in substring already
                if len(tset) == 0 and r - l < sublen:
                    sublen = r - l
                    indexes = (l, r+1) # for string slice at the end
                print(s[indexes[0]:indexes[1]], l, r)
            r += 1
        
        return s[indexes[0]:indexes[1]]
        

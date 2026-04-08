class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        ## sliding window thru string. 
        ## keep history of chars and their indexes in a dict
        ## when it comes to a repeated char, replace its index in the dict
        ## also track longest substring with dict 
        l, r = 0, 1
        history = defaultdict(int)

        # initialize first element
        history[s[l]] = 0

        longest = 1

        while r < len(s):
            # 2 CASES: either you run into a repeated char or you dont.
            # repeated: l becomes the last repeated chars index
            if s[r] in history:
                if l <= history[s[r]]:
                    l = history[s[r]] + 1
            history[s[r]] = r

            if r - l + 1 > longest:
                longest = r - l + 1
            
            r += 1
        return longest

            

             

        
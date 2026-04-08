class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        # sliding window
        # r just keeps incrementing
        # l increments when r comes accross a duplicate
        # use a hashmap to track length and index
        window = {}
        max_len = 1
        l, r = 0, 0 
        while r < len(s):
            char = s[r]
            if char in window and window[char] >= l:
                l = window[char] + 1 # set to one past
            
            # add new char to window
            window[char] = r
            r += 1
            
            # update new max len
            max_len = max(max_len, r-l)
        return max_len
            

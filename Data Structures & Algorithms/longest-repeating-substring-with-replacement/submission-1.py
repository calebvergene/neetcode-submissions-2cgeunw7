class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## Use a sliding window with a hashmap
        ## The hashmap counts the letter frequency of each char in the window
        ## Then, you can see if (length of window) - (most freq letter) <= k
        ## When this is >, then you need to increment left side
        l, r = 0, 0
        window_hash = defaultdict(int)
        window_hash[s[0]] += 1 # init first element
        longest = 0
        while r < len(s):
            # increment r when len - freq <= k (can keep expanding window)
            # increment l when len - freq > k (need to shrink window)

            ## this returns char with the highest count
            highest_freq = max(window_hash.values())
            window_len = r - l + 1

            if window_len - highest_freq <= k:
                longest = max(longest, window_len)
                r += 1
                if r < len(s):
                    window_hash[s[r]] += 1 ## add new element to hash
            else:
                window_hash[s[l]] -= 1 ## remove first element because increase l
                l += 1
        return longest
        
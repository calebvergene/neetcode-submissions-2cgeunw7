class Solution:
    def numDecodings(self, s: str) -> int:
        # ways increases if the numbers can be combined. 
        # if combined, ways = (i+1)+(i+2)
        memo = {len(s):1}
        if s[0] == "0": return 0

        def decode(index):
            # top to bottom approach
            # base case: 1 out of bound or already exists in the cache
            if index in memo:
                return memo[index]
            # if come across a 0, needs to be connected at the front. basically skip
            if s[index] == '0':
                memo[index] = 0
                return 0

            # basically, starting from the end, calculate ways for each letter then store it
            ways = decode(index+1)

            # if i and i+1 can be combined, then you need to calculate the # of ways for (i+1) and (i+2)
            # which should be already stored. 
            if index+2 <= len(s) and (int(s[index])*10) + int(s[index+1]) <= 26:
                ways += decode(index+2)

            # store ways then return it
            memo[index] = ways
            return ways
        return decode(0)
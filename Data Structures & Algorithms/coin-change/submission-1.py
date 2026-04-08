class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        # DP, store an array to keep track of shortest amount of coins for each coin
        memoiz = [-1] * (amount+1)
        # base case, start the memoiz list with coins we know
        for coin in coins:
            if coin in range(amount+1):
                memoiz[coin] = 1

        # now, starting at 1, track min amount of coins you can make
        for i in range(amount+1):
            # look at previous coins. choose the previous coin path where adding 
            # a specific coin would give you the smallest amount of coins.

            # we can do this by subtracting in memoiz to see the most optimal and possible path.
            mincoins = float('inf')
            for coin in coins:
                # in bounds check, amount is possible to be made, and index i is not a starting coin val
                if i - coin >= 0 and memoiz[i-coin] != -1 and memoiz[i] == -1:
                    mincoins = min(mincoins, memoiz[i-coin])

            if mincoins != float('inf'):
                # then we found a coin that can be made
                memoiz[i] = mincoins + 1

        return memoiz[-1]
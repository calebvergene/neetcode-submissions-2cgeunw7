class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        # keep left the highest with right lowest. 
        # keep sliding window to find max profit
        l, r = 0, 1
        while r < len(prices):
            ## determine if window is max profit
            if prices[r] - prices[l] > max_profit:
                max_profit = prices[r] - prices[l] 
            ## iters thru prices. if right(sell) is less than left(buy), 
            ## then left becomes right. This basically makes buy always the 
            ## lowest value. 
            if prices[r] < prices[l]:
                l = r
            r += 1
        return max_profit

        
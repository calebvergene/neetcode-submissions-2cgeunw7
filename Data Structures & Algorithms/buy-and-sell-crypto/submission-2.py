class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # l is always the minimum. r just increments
        
        l, r = 0, 0 
        while r < len(prices):
            # curr day is less than l
            if prices[r] < prices[l]:
                l = r
            else:
                # calculate the current profit 
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            
            r += 1
        
        return max_profit

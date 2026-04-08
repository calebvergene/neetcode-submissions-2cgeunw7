class StockSpanner:

    def __init__(self):
        # if you pop from the stack, its stored in the next span
        self.stack = [] # (price, span)
        

    def next(self, price: int) -> int:
        # in stack, store a days price and span
        # storing the span eliminates repeated work of recounting. 
        span = 1
        while self.stack:
            prev = self.stack[-1]
            if prev[0] <= price:
                self.stack.pop()
                span += prev[1]
            else:
                break
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
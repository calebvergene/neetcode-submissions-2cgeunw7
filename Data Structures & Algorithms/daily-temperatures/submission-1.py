class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack of only increasing
        # stack elements are (temp, index)
        # update output result only when you pop that index from the stack 

        stack, res = [], [0]*len(temperatures)
        for day, temp in enumerate(temperatures):
            # remove all lower, then add to stack
            while stack and stack[-1][0] < temp:
                popped = stack.pop()
                res[popped[1]] = day - popped[1]
            stack.append((temp, day))
        return res

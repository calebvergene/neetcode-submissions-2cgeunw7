class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        final = []
        # exit when len of curr = k
        # iterate through range n
        def backtrack(curr, start):
            if len(curr) == k:
                final.append(curr[:])
                return
            
            for i in range(start, n+1):
                curr.append(i)
                backtrack(curr, i+1)
                curr.pop()
        backtrack([], 1)
        return final
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(num):
            if num >= n:
                return num == n
            return dfs(num+1) + dfs(num+2)
        return dfs(0)
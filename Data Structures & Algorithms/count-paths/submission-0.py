class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # for top down dynamic programming, you know you are going to be going over a lot
        # of the same subpaths

        # so, when fully traversing all paths from a square, add that square to a finshed dict.
        # with the amount of different paths it could have

        # BASICALLY: EACH SQUARES NUMBER OF WAYS ARE its right + bottom 
        # similar to like: a square can either go down or right, so call dfs(down) + dfs(right) 
        
        reached = {}
        # rows, cols = n, m

        def dfs(row, col):
            # base case
            if row == n-1 and col == m-1:
                return 1
            # check if we have already visited the square, because then we know # of ways 
            if (row, col) in reached:
                return reached[(row, col)]
            
            # recursive call on bottom and right
            ways = 0
            # bounds checking to move on to next square
            if row+1 in range(n):
                ways += dfs(row+1, col)
            if col+1 in range(m):
                ways += dfs(row, col+1)
            
            # now here, we have iterated all possible paths from the square. add to dict then return
            reached[(row,col)] = ways
            return ways
        
        return dfs(0,0)
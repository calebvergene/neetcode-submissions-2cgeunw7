class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        # now we need to find the number of fresh fruit and then store the pos of the rotten fruit
        q = collections.deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        # now we can start bfs
        minutes = 0
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)): # this is to iterate once per minute
                rotten = q.popleft()

                # now we make every fruit around this fruit rotten 
                for direction in directions:
                    next_r = rotten[0] + direction[0]
                    next_c = rotten[1] + direction[1]
                    if next_r in range(ROWS) and next_c in range(COLS) and grid[next_r][next_c] == 1:
                        # then we found a fresh fruit adjacent to this rotten fruit!
                        # make that fruit rotten and decrease fresh counter
                        grid[next_r][next_c] = 2
                        fresh -= 1
                        q.append([next_r, next_c])
        
        return minutes if fresh == 0 else -1
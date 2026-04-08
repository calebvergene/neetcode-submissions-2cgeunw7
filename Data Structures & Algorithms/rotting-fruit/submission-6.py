class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # - need to do multi source bfs for each rotten fruit in the grid
        # and track each minute / level (with for loop) 
        # - then from there see how many fresh fruit you hit. keep a tracker
        # to know if you hit every fresh fruit possible. 
        rows, cols = len(grid), len(grid[0])
        fruits = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        q = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fruits += 1
                elif grid[row][col] == 2:
                    fruits += 1
                    q.append((row, col)) # append rotten fruit
        # now start bfs
        minutes = 0
        while q:
            # allows us to increment minutes for each move
            for _ in range(len(q)):
                frow, fcol = q.popleft()
                fruits -= 1
                for x, y in directions:
                    if (0 <= frow+x < len(grid) 
                    and 0 <= fcol+y < len(grid[0])
                    and grid[frow+x][fcol+y] == 1):
                        grid[frow+x][fcol+y] = 2
                        q.append((frow+x,fcol+y))
            if q: minutes += 1
        return minutes if fruits == 0 else -1
                        



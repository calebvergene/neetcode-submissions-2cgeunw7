class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0, -1], [1,0], [-1,0]]
        
        # find the treasure chests first and then bfs
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # we found a chest
                    q.append([r,c])
        
        # now BFS starting at ALL chests simultaneously
        # traverse through grid. if distance is less than grid val, 
        # then cell = distance. this finds smallest distance from a chest
        dis = 0
        while q:
            dis += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                
                # now traverse each direction and add back into queue
                for direction in directions:
                    nr, nc = r + direction[0], c + direction[1]
                    
                    if (nr in range(rows) and nc in range(cols) and 
                        grid[nr][nc] > dis):
                        
                        # then valid cell to traverse
                        grid[nr][nc] = dis
                        q.append([nr, nc])
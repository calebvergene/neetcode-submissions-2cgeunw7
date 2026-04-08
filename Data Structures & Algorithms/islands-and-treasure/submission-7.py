class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0, -1], [1,0], [-1,0]]
        
        # start at the treasure chests and BFS all possible land cells
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
        
        # now start bfs from each chest
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft() # cell

                for direct in directions:
                    new_r, new_c = r + direct[0], c + direct[1]
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 2147483647:
                        grid[new_r][new_c] = dist
                        q.append([new_r, new_c])
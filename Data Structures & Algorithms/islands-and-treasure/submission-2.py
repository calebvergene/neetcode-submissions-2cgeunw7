class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0, -1], [1,0], [-1,0]]
        # find the treasure chests first and then bfs
        chests = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # we found a chest
                    chests.append([r,c])
        # now BFS starting at each chest
        for chest in chests: # in [r,c] format
            visited = set(tuple(chest))
            q = collections.deque()
            distance = 0
            q.append(chest)
            # traverse through grid. if distance is less than grid val, 
            # then cell = distance. this finds smallest distance from a chest
            while q:
                # this for loop is to get the distance from the chest
                distance += 1
                for _ in range(len(q)):
                    r, c = q.popleft()
                    # now traverse each direction and add back into queue
                    for direction in directions:
                        if r + direction[1] in range(rows) and c + direction[0] in range(cols) and (r + direction[1], c + direction[0]) not in visited:
                            next_cell = grid[r + direction[1]][c + direction[0]]
                            if next_cell != -1:
                                # then valid cell to traverse
                                if next_cell > distance:
                                    grid[r + direction[1]][c + direction[0]] = distance
                                q.append([r + direction[1], c + direction[0]])
                                visited.add((r + direction[1], c + direction[0]))
        
                        
                        
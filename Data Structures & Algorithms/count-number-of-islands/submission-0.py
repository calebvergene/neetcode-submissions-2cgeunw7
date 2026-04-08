class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r, c):
            if (r, c) in visited or grid[r][c] == '0':
                return
            visited.add((r,c))
            for direction in directions:
                if direction[0] + c in range(cols) and direction[1] + r in range(rows):
                    dfs(direction[1] + r, direction[0] + c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands
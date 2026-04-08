class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = ((0,1), (1,0), (0,-1), (-1,0))

        # use dfs to find all paths that would work
        def dfs(cell, ocean): # cell = (r,c)
            if cell in ocean:
                return
            ocean.add(cell)
            for r, c in directions:
                # check out of bounds and if next cell greater
                nextr, nextc = cell[0]+r, cell[1]+c
                if nextr in range(rows) and nextc in range(cols):
                    if heights[nextr][nextc] >= heights[cell[0]][cell[1]]:
                        dfs((nextr, nextc), ocean)
        
        # up and down
        for c in range(cols):
            dfs((0,c), pacific)
            dfs((rows-1,c), atlantic)
        for r in range(rows):
            dfs((r, 0), pacific)
            dfs((r,cols-1), atlantic)
        
        reaches = pacific & atlantic
        return [list(cell) for cell in reaches]

        
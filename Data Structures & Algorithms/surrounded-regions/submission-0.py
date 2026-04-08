class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find O cells that are not surrounded. 
        # this is basically the O cells that are on the border
        # and the O cells that are connected to the border O cells in the same group.
        rows, cols = len(board), len(board[0])
        safe = set()
        directions = ((0,1), (1,0), (-1,0), (0,-1))

        def dfs(cell, safe):
            if cell in safe or board[cell[0]][cell[1]] != 'O':
                return 
            safe.add(cell)
            for r, c in directions:
                newr, newc = cell[0]+r, cell[1]+c
                # in bounds
                if newr in range(rows) and newc in range(cols):
                    dfs((newr,newc), safe)
        
        # get border Os
        for r in range(rows):
            dfs((r, 0), safe)
            dfs((r, cols-1), safe)
        for c in range(cols):
            dfs((0, c), safe)
            dfs((rows-1, c), safe)
        # remaining non-border cells that are not safe need to all be "X"
        for r in range(1, len(board)-1):
            for c in range(1, len(board[0])-1):
                if (r, c) not in safe:
                    board[r][c] = "X"
                
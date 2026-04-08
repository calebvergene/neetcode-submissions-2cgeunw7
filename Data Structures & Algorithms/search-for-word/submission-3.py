class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        found = False
        # use dfs recursion
        def dfs(row, col, i):
            nonlocal visited, found
            # alr found or bad path
            if found or board[row][col] != word[i]:
                return
            # word was found then
            if len(word)-1 == i:
                found = True
                return
            visited.add((row,col))
            # so then we did find the next letter
            for r, c in directions:
                if row + r in range(len(board)) and col + c in range(len(board[0])) and (row+r,col+c) not in visited:
                    dfs(row+r, col+c, i+1)
            visited.remove((row, col))
        for r in range(len(board)):
            for c in range(len(board[0])):
                if not found:
                    visited = {(r,c)}
                    dfs(r, c, 0)
        return found
                
                    
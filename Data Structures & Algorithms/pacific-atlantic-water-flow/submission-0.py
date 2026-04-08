class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs
        directions = [(0,-1),(-1,0),(1,0),(0,1)] # go left and up first
        rows, cols = len(heights), len(heights[0])
        reaches = set()
        coord_reached = []

        def dfs(row, col):
            nonlocal coord_reached, visited
            if coord_reached == [True, True]:
                return
            visited.add((row,col))

            for r, c in directions:
                print(row, col)
                if row + r < 0 or col + c < 0:
                    print("reached pacific")
                    coord_reached[0] = True
                elif row + r == rows or col + c == cols:
                    print("reached atlantic")
                    coord_reached[1] = True
                else:
                    if heights[row + r][col + c] <= heights[row][col] and (row + r,col + c) not in visited:
                        if (row + r, col + c) in reaches:
                            coord_reached = [True, True]
                            return
                        dfs(row + r, col + c)
        
        for r in range(rows):
            for c in range(cols):
                coord_reached = [False, False]
                visited = set()
                print("WORKING WITH", (r, c))
                dfs(r, c)
                if coord_reached == [True, True]:
                    print((r, c), "reached both")
                    reaches.add((r,c))
        return [[r,c] for r,c in reaches]

        
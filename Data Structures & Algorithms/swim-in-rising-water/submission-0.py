class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        # tuple (row, col, max)
        heapq.heappush(heap, (grid[0][0],0,0))

        while True:
            node = heapq.heappop(heap)
            row, col = node[1],node[2]
            grid[row][col] = -1
            for direction in directions:
                newr, newc = row + direction[0], col + direction[1]
                if newr in range(len(grid)) and newc in range(len(grid[0])):
                    if newr == len(grid)-1 and newc == len(grid[0]) - 1:
                        return max(node[0], grid[newr][newc])
                    if grid[newr][newc] != -1:
                        heapq.heappush(heap, (max(node[0],grid[newr][newc]),newr, newc))
                    

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # right, down, left, up 
        directions = [[0,1], [1,0], [0,-1],[-1,0]]
        res = [matrix[0][0]]
        matrix[0][0] = "x"

        ROWS, COLS = len(matrix), len(matrix[0])
        row, col = 0, 0
        while len(res) < ROWS*COLS:
            for direction in directions:
                while (0 <= row + direction[0] < ROWS and  0 <= col+direction[1] < COLS):
                    if matrix[row + direction[0]][col+direction[1]] == "x":
                        break
                    row += direction[0]
                    col += direction[1]
                    res.append(matrix[row][col])
                    matrix[row][col] = "x"
        return res

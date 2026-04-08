class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # when you come accross a 0, you can make col above and row to the left 0
        # continue iterating row, turning everything to 0.

        # then, if you ever come accross a square underneath a 0, turn that to 0. 

        def helper(row, col):
            # up and down
            for i in range(0, len(matrix)):
                if matrix[i][col]:
                    matrix[i][col] = "x"
            # left 
            for j in range(0, col):
                if matrix[row][j]:
                    matrix[row][j] = "x"
            
        
        for r in range(len(matrix)):
            found = False
            for c in range(len(matrix[0])):
                # up, down, and left
                if matrix[r][c] == 0:
                    helper(r, c)
                    found = True
                # right 
                if found:
                    matrix[r][c] = "x"

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "x":
                    matrix[r][c] = 0        

                
            
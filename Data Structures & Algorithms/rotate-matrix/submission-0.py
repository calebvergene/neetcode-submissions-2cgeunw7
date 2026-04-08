class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # just transpose then reverse 

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                # to transpose in place, you need to swap
                # its always a square matrix, so you only want to swap
                # the top right half of the matrix 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # now reverse 
        for row in matrix:
            row.reverse()
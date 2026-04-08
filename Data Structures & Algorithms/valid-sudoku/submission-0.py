class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # basically, check each 3x3 square
        # then each time add to hash set for rows and cols to see if you have a repeating num 

        rowhash = collections.defaultdict(set)
        colhash = collections.defaultdict(set)

        for section in range(3):
            for cube in range(3):
                squareset = set()
                for r in range(3):
                    for c in range(3):
                        square = board[r + section*3][c + cube*3]
                        if square == ".":
                            continue
                        elif square in squareset:
                            return False
                        squareset.add(square)
                        # now we need to determine what hash to add to 
                        if square in rowhash[r + section*3]:
                            return False 
                        rowhash[r + section*3].add(square)
                        if square in colhash[c + cube*3]:
                            return False 
                        colhash[c + cube*3].add(square)
        # makes it thru, then good to go 
        return True 



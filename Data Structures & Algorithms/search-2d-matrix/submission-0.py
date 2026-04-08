class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # this problem is like a nested binary search. 
        ## first find what row it is in with binary search 
        l, r = 0, len(matrix) - 1
        while (l <= r):
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        found = r
        ## ok we learned this in binary search for inserting in an array in 46
        ## if not found, r will end up barley less than target, and l will end 
        ## up barely greater than target, as that is when the while loop ends. 
        ## now binary search in the found array. 
        l, r = 0, len(matrix[found]) - 1
        while (l <= r):
            mid = (l + r) // 2
            if matrix[found][mid] == target:
                return True
            elif matrix[found][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        
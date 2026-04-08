class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(curr, i):
            if len(curr) == len(digits):
                res.append(curr)
                return 
            
            for letter in digitToChar[digits[i]]:
                backtrack(curr+letter, i+1) # i is the digit you point to, so i+1
        
        backtrack("", 0)
        return res

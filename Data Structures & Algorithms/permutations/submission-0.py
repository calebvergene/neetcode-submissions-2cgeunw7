class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current, remaining):
            if not remaining:
                res.append(current[:])
                return
            
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()
            
            return
        backtrack([], nums)
        return res
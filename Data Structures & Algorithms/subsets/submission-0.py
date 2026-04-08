class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        def backtrack(current, remaining):
            final.append(current[:])
            if not remaining:
                return
            
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[i+1:])
                current.pop()
        backtrack([], nums)
        return final
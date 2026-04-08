class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # so order does matter 
        res = []

        def backtrack(rest, curr):
            res.append(curr[:])
            for i, num in enumerate(rest):
                curr.append(num)
                backtrack(rest[i+1:], curr)
                curr.pop()
        backtrack(nums, [])
        return res
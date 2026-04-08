class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = set()
        nums.sort()
        single = set()
        def backtrack(remaining, curr):
            final.add(tuple(curr))
            if len(remaining) == 0:
                return
            
            for i in range(len(remaining)):
                if not len(curr):
                    if remaining[i] in single:
                        continue
                    single.add(remaining[i])
                curr.append(remaining[i])
                backtrack(remaining[i+1:], curr)
                curr.pop()
        backtrack(nums, [])
        return [list(subset) for subset in final]
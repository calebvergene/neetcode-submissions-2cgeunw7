class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def backtrack(start, curr):
            result.append(curr[:])
            
            for i in range(start, len(nums)):
                # Skip duplicates: if current number equals previous AND
                # we're not at the start position, skip it
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return result
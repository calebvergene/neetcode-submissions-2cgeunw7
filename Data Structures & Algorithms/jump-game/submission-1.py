class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # iterate through nums, and store the farthest you could possibley jump to. 
        # calc that max distance each step.
        max_dist = pos = 0
        while pos <= max_dist and pos < len(nums):
            max_dist = max(pos + nums[pos], max_dist)
            pos += 1
        
        return True if pos == len(nums) else False
        
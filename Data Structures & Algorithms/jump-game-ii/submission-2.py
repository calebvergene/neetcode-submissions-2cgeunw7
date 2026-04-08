class Solution:
    def jump(self, nums: List[int]) -> int:
        # at each index, just keep track of the maxiumum distance you can reach. 
        # each time you need to jump, then increment jump counter. 
        i = 0 
        jumps = 0
        curr_jump, max_jump = nums[0], 0
        while i < len(nums)-1:
            # find the max distance for next jump at each jump
            while i < len(nums)-1 and i < curr_jump:
                i += 1
                max_jump = max(max_jump, i + nums[i])
            curr_jump = max_jump
            jumps += 1
        
        return jumps

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        starters = []
        for num in nums:
            if num-1 not in nums:
                starters.append(num)
        
        max_sequence = 1
        for starter in starters:
            curr_sequence = 1
            num = starter
            while num + 1 in nums:
                curr_sequence += 1
                num += 1
            max_sequence = max(curr_sequence, max_sequence)
        
        return max_sequence

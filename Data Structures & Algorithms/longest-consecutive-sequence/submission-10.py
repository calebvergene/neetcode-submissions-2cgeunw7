class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums = set(nums)
        longest = 1

        for num in nums:
            if num-1 not in nums:
                # then it is a starter number 
                length = 1
                while (num + length in nums):
                    length += 1
                longest = max(longest, length)
        return longest



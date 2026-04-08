class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        if len(nums) > 0:
            longest = 1

        for num in nums:
            if num - 1 not in nums:
                count = 1
                while (num + count in nums):
                    count += 1 
                    if count > longest:
                        longest = count
            
        return longest
        